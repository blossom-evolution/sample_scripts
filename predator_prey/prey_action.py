import random
import numpy as np


def prey(organism, population_dict, world, position_hash_table=None):
    # choice = random.randrange(0, 20)
    if np.random.rand() < 1/30:
        return 'reproduce'
    else:
        return 'move'


def only_drink(organism, population_dict, world, position_hash_table=None):
    return 'drink'


def only_eat(organism, population_dict, world, position_hash_table=None):
    return 'eat'


def dumb_predator(organism, population_dict, world, position_hash_table=None):
    choice = random.randrange(0, 5)
    if choice == 0:
        return 'eat'
    elif choice == 1:
        return 'drink'
    elif choice >= 2 and choice <= 3:
        return 'reproduce'
    else:
        return 'move'


def fast_reproduce(organism, population_dict, world, position_hash_table=None):
    choice = random.randrange(0, 3)
    if choice == 0 and organism.water_current > 10:
        return 'reproduce'
    elif choice == 1:
        return 'move'
    else:
        return 'drink'


def fast_actions_predator(organism, population_dict, world, position_hash_table=None):
    if random.randrange(0, 10) < 4:
        choice = random.randrange(0, 5)
        if choice == 0:
            return 'reproduce'
        elif choice == 1:
            return 'move'
        elif choice in [2, 3]:
            return 'eat'
        else:
            return 'drink'
    else:
        return 'move'


def try_to_live_predator(organism, population_dict, world, position_hash_table=None):
    if organism.water_current == 0:
        return 'drink'
    elif organism.food_current == 0:
        return 'eat'
    else:
        return fast_actions_predator(organism, population_dict, world, position_hash_table=None)


def fast_actions_prey(organism, population_dict, world, position_hash_table=None):
    if random.randrange(0, 10) < 4:
        choice = random.randrange(0, 4)
        if choice == 0:
            if random.randrange(0, 10) < 10:
                return 'reproduce'
            else:
                return 'move'
        elif choice == 1:
            return 'move'
        elif choice == 2:
            return 'eat'
        else:
            return 'drink'
    else:
        return 'move'


def try_to_live_prey(organism, population_dict, world, position_hash_table=None):
    if organism.water_current == 0:
        return 'drink'
    elif organism.food_current == 0:
        return 'eat'
    else:
        return fast_actions_prey(organism, population_dict, world, position_hash_table=None)


def move_to_live(organism, population_dict, world, position_hash_table=None):
    if organism.water_current == 0:
        if world.water[organism.position[0]] > 0:
            return 'drink'
        else:
            return 'move'
    elif organism.food_current == 0:
        if world.food[organism.position[0]] > 0:
            return 'eat'
        else:
            return 'move'
    elif organism.water_current > organism.water_capacity // 2 \
            and organism.food_current > organism.food_capacity // 2:
        return 'reproduce'
    else:
        choice = random.randrange(0, 3)
        if choice == 0:
            return 'move'
        elif choice == 1:
            return 'eat'
        else:
            return 'drink'


def move_to_live_2d(organism, population_dict, world, position_hash_table=None):
    if organism.water_current == 0:
        if world.water[organism.position[0]][organism.position[1]] > 0:
            return 'drink'
        else:
            return 'move'
    elif organism.food_current == 0:
        if world.food[organism.position[0]][organism.position[1]] > 0:
            return 'eat'
        else:
            return 'move'
    else:
        choice = random.randrange(0, 4)
        if choice == 0:
            return 'move'
        elif choice == 1:
            return 'eat'
        elif choice == 2:
            return 'drink'
        else:
            if organism.water_current > organism.water_capacity // 2 \
                    and organism.food_current > organism.food_capacity // 2:
                return 'reproduce'
            else:
                return 'move'
