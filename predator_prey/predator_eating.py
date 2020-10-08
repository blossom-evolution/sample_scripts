import random


def eat_prey1(organism, population_dict, world, position_hash_table=None):
    position = tuple(organism.position)
    colocated_prey = []
    colocated_predators = []
    for org in position_hash_table[position]:
        if org.alive:
            if org.species_name == 'prey1':
                colocated_prey.append(org)
            elif org.species_name == 'predator1':
                colocated_predators.append(org)
    if len(colocated_prey) == 0 or len(colocated_prey) <= len(colocated_predators):
        return [organism]
    elif len(colocated_prey) == 1:
        prey = colocated_prey[0]
    else:
        prey = colocated_prey[random.randrange(0, len(colocated_prey))]

    food_from_prey = 0.8 * (prey.food_capacity)
    diff = organism.food_capacity - organism.food_current
    intake = min(food_from_prey, diff)
    organism = organism.update_parameter('food_current',
                                         intake,
                                         method='add')

    prey = prey.die('eaten')

    return [organism, prey]
