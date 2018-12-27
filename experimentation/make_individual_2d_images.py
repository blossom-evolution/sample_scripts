import os, sys, errno
import glob
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/blossom')
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/flowerpot')

import imageio
import numpy as np
import json
import matplotlib.pyplot as plt

from blossom import *
from flowerpot import *

time = 200
DATASET_OUTPUT_DIR = 'datasets/experimentation'

organism_fields = ['alive', 'old_age', 'thirst', 'hunger', 'births']
world_fields = ['water', 'food']
organism_paths = sorted(glob.glob('%s/organisms_ds????.txt' % DATASET_OUTPUT_DIR))
world_paths = sorted(glob.glob('%s/world_ds????.txt' % DATASET_OUTPUT_DIR))

with open(world_paths[0], 'r') as f:
    world = json.load(f)

world_size = world['world_size']

images_dir = 'images'
gifs_dir = 'gifs'
for dir in [images_dir, gifs_dir]:
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

for field in organism_fields:
    for i in range(time + 1):
        max_val = 0

        plot = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

        with open(organism_paths[i], 'r') as f:
            organism_list = json.load(f)

        for organism in organism_list:
            if field == 'alive' and organism['alive'] \
            or field == 'old_age' and organism['cause_of_death'] == 'old_age' \
            or field == 'thirst' and organism['cause_of_death'] == 'thirst' \
            or field == 'hunger' and organism['cause_of_death'] == 'hunger' \
            or field == 'births' and organism['age'] == 0:
                plot[organism['position'][0]][organism['position'][1]] += 1

        for j in plot:
            for i in j:
                if i > max_val:
                    max_val = i

    for i in range(time + 1):
        plt.close('all')

        plot = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

        with open(organism_paths[i], 'r') as f:
            organism_list = json.load(f)

        for organism in organism_list:
            if field == 'alive' and organism['alive'] \
            or field == 'old_age' and organism['cause_of_death'] == 'old_age' \
            or field == 'thirst' and organism['cause_of_death'] == 'thirst' \
            or field == 'hunger' and organism['cause_of_death'] == 'hunger' \
            or field == 'births' and organism['age'] == 0:
                plot[organism['position'][0]][organism['position'][1]] += 1

        fig = plt.figure()
        plt.imshow(plot)
        plt.title('Time: %03d' % i)
        plt.clim(0, max_val)
        plt.colorbar()
        plt.savefig('%s/image_2d_%s_%03d.png' % (images_dir, field, i))
        print(field, i)

for field in world_fields:
    for i in range(time + 1):
        max_val = 0

        plot = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

        with open(world_paths[i], 'r') as f:
            world = json.load(f)

        plot = world[field]

        for j in plot:
            for i in j:
                if i > max_val:
                    max_val = i

    for i in range(time + 1):
        plt.close('all')

        plot = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

        with open(world_paths[i], 'r') as f:
            world = json.load(f)

        plot = world[field]

        fig = plt.figure()
        plt.imshow(plot)
        plt.title('Time: %03d' % i)
        plt.clim(0, max_val)
        plt.colorbar()
        plt.savefig('%s/image_2d_%s_%03d.png' % (images_dir, field, i))
        print(field, i)

for field in (organism_fields + world_fields):
    filenames = sorted(glob.glob('%s/image_2d_%s_???.png' % (images_dir, field)))

    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))

    imageio.mimsave('%s/%s.gif' % (gifs_dir, field), images, duration=0.1)
    print('%s gif saved!' % field)
