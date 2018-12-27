import random


def eat_prey1(organism, organism_list, world, position_hash_table=None):
    position = tuple(organism.position)
    colocated = []
    for org in position_hash_table[position]:
        if org.species_name == 'prey1':
            colocated.append(org)
    if len(colocated) == 0:
        return [organism]
    elif len(colocated) == 1:
        prey = colocated[0]
    else:
        prey = colocated[random.randrange(0, len(colocated))]

    food_from_prey = 0.8 * (prey.food_capacity)
    diff = organism.food_capacity - organism.food_current
    intake = min(food_from_prey, diff)
    organism.food_current += intake

    prey = prey.die('eaten')

    return [organism, prey]
