from context import blossom

import world_params

ENVIRONMENT_FN = 'generated_environment.json'

# Set up world
world_size = world_params.world_dict['world_size']

peak_water = 1000
water = [[peak_water // 2 for x in range(world_size[1])]
         for y in range(world_size[0])]
for i in range(world_size[0] // 4, 3 * world_size[0] // 4,):
    water[i] = [peak_water] * world_size[1]

peak_food = 1000
food = [([peak_food // 2 for x in range(world_size[1] // 4)]
         + [peak_food for x in range(world_size[1] // 2)]
         + [peak_food // 2 for x in range(world_size[1] // 4)])
        for y in range(world_size[0])]

obstacles = [[0 for x in range(world_size[1])] for y in range(world_size[0])]

blossom.write_environment(water,
                          food,
                          obstacles,
                          ENVIRONMENT_FN)
