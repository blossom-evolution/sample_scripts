"""Predator-prey custom behaviors using Blossom's native intent API."""

from __future__ import annotations

from blossom.simulation import (
    BehaviorContext,
    CompositeIntent,
    FieldChange,
    OrganismView,
    UpdateIntent,
)


PREDATOR_SPECIES = "predator"
PREY_SPECIES = "prey"


def prey_action(org: OrganismView, ctx: BehaviorContext) -> str:
    """Simple prey policy: mostly move, occasionally reproduce.

    Args:
        org: Read-only actor view.
        ctx: Read-only behavior context.

    Returns:
        Chosen built-in action name.
    """
    del org
    if ctx.rng.random() < (1.0 / 30.0):
        return "reproduce"
    return "move"


def predator_action(org: OrganismView, ctx: BehaviorContext) -> str:
    """Choose predator action based on local prey and hunger state.

    Args:
        org: Read-only actor view.
        ctx: Read-only behavior context.

    Returns:
        Chosen action (`move`, `eat`, or `reproduce`).
    """
    colocated_prey = [
        prey
        for prey in ctx.at_location(tuple(org.location))
        if prey.alive and prey.species_name == PREY_SPECIES
    ]

    food_capacity = float(org.food_capacity or 0)
    food_current = float(org.food_current or 0)
    is_well_fed = food_current >= 0.5 * food_capacity

    if colocated_prey:
        if ctx.rng.random() < 0.12 and is_well_fed:
            return "reproduce"
        return "eat"
    return "move"


def eat_prey(org: OrganismView, ctx: BehaviorContext) -> CompositeIntent:
    """Return a predator-eating composite intent for the actor.

    Args:
        org: Read-only actor view.
        ctx: Read-only behavior context.

    Returns:
        Intent payload that updates predator energy and prey alive state.
    """
    colocated = ctx.at_location(tuple(org.location))
    colocated_prey = [
        prey
        for prey in colocated
        if prey.alive and prey.species_name == PREY_SPECIES
    ]
    colocated_predators = [
        predator
        for predator in colocated
        if predator.alive and predator.species_name == PREDATOR_SPECIES
    ]

    if not colocated_prey or len(colocated_prey) <= len(colocated_predators):
        return CompositeIntent(
            actor_id=org.organism_id,
            updates=(UpdateIntent(organism_id=org.organism_id, changes=()),),
        )

    prey = colocated_prey[0]
    if len(colocated_prey) > 1:
        prey = ctx.rng.choice(colocated_prey)

    food_from_prey = 0.8 * float(prey.food_capacity or 0)
    diff = max(float(org.food_capacity or 0) - float(org.food_current or 0), 0.0)
    intake = min(food_from_prey, diff)

    return CompositeIntent(
        actor_id=org.organism_id,
        updates=(
            UpdateIntent(
                organism_id=org.organism_id,
                changes=(FieldChange(field="food_current", op="add", value=intake),),
            ),
            UpdateIntent(
                organism_id=prey.organism_id,
                changes=(
                    FieldChange(field="alive", op="set", value=False),
                    FieldChange(field="cause_of_death", op="set", value="eaten"),
                    FieldChange(field="age_at_death", op="set", value=prey.age),
                ),
            ),
        ),
    )
