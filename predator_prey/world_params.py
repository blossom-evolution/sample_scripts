# This is the parameter file for the initial world environment.
import math

world_dict = {}

# # Dimensionality (int)
world_dict['dimensionality'] = 2

# Size of world (ints with correct dimensionality, or 'None')
# example: world_size = 10 10
world_dict['world_size'] = [1, 4]
# world_dict['world_size'] = 20

# Filename for environment specification (str, or 'None')
# world_dict['environment_filename'] = 'generated_environment.json'

# Set up world
world_size = world_dict['world_size']

peak_water = math.inf
water = [[peak_water
          for x in range(world_size[1])]
         for y in range(world_size[0])]

# water = [peak_water for x in range(world_size)]

peak_food = math.inf
food = [[peak_food
         for x in range(world_size[1])]
        for y in range(world_size[0])]

# food = [peak_food for x in range(world_size)]

# peak_water = 1000
# water = [[peak_water // 2 for x in range(world_size[1])]
#          for y in range(world_size[0])]
# for i in range(world_size[0] // 4, 3 * world_size[0] // 4,):
#     water[i] = [peak_water] * world_size[1]
#
# peak_food = 1000
# food = [([peak_food // 2 for x in range(world_size[1] // 4)]
#          + [peak_food for x in range(world_size[1] // 2)]
#          + [peak_food // 2 for x in range(world_size[1] // 4)])
#         for y in range(world_size[0])]

obstacles = [[0 for x in range(world_size[1])] for y in range(world_size[0])]

# obstacles = [0 for x in range(world_size)]

world_dict['water'] = water
world_dict['food'] = food
world_dict['obstacles'] = obstacles
