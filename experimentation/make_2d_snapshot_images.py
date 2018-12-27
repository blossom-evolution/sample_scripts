import os, sys, errno
import glob
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/blossom')
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/flowerpot')

import imageio
import numpy as np
import json

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from blossom import *
from flowerpot import *

time = 200
frame_duration = 0.1  # sec
DATASET_OUTPUT_DIR = 'datasets/longer'

organism_paths = sorted(glob.glob('%s/organisms_ds????.txt'
                                  % DATASET_OUTPUT_DIR))[:(time + 1)]
world_paths = sorted(glob.glob('%s/world_ds????.txt' % DATASET_OUTPUT_DIR))[:(time + 1)]

with open(world_paths[0], 'r') as f:
    world = json.load(f)

world_size = world['world_size']

maxes = []

for field in ['alive']:
    max_val = 0

    for i in range(time + 1):

        plot = [[0 for x in range(world_size[1])]
                for x in range(world_size[0])]

        with open(organism_paths[i], 'r') as f:
            organism_list = json.load(f)

        for organism in organism_list:
            if field == 'alive' and organism['alive']:
                plot[organism['position'][0]][organism['position'][1]] += 1

        for j in plot:
            for i in j:
                if i > max_val:
                    max_val = i

    maxes.append(max_val)

for field in ['water', 'food']:
    max_val = 0

    for i in range(time + 1):

        plot = [[0 for x in range(world_size[1])]
                for x in range(world_size[0])]

        with open(world_paths[i], 'r') as f:
            world = json.load(f)

        plot = world[field]

        for j in plot:
            for i in j:
                if i > max_val:
                    max_val = i

    maxes.append(max_val)

print('Found maxes...')

# Make images
for t in range(time + 1):
    plt.close('all')

    total = 0

    organism_path = organism_paths[t]
    world_path = world_paths[t]

    fig = plt.figure(constrained_layout=True, figsize=(10, 10))
    gs = gridspec.GridSpec(ncols=4, nrows=4, figure=fig)

    ax0 = fig.add_subplot(gs[0:2, 0:2])
    plt.sca(ax0)
    with open(organism_path, 'r') as f:
        organism_list = json.load(f)
    with open(world_path, 'r') as f:
        world = json.load(f)

    world_size = world['world_size']
    plot = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

    for organism in organism_list:
        if organism['alive']:
            plot[organism['position'][0]][organism['position'][1]] += 1
            total += 1

    plt.imshow(plot)
    plt.title('Living Organisms')
    plt.clim(0, maxes[0])
    plt.colorbar()

    ax1 = fig.add_subplot(gs[2:4, 0:2])
    plt.sca(ax1)
    with open(world_path, 'r') as f:
        world = json.load(f)

    plot = world['water']

    plt.imshow(plot)
    plt.title('Water Supply')
    plt.clim(0, maxes[1])
    plt.colorbar()

    ax2 = fig.add_subplot(gs[2:4, 2:4])
    plt.sca(ax2)
    with open(world_path, 'r') as f:
        world = json.load(f)

    plot = world['food']

    plt.imshow(plot)
    plt.title('Food Supply')
    plt.clim(0, maxes[2])
    plt.colorbar()

    ax = fig.add_subplot(gs[0:2, 2:4], frameon=False)
    plt.sca(ax)
    ax.annotate('Timestep: %04d' % t, xy=(0.5, 0.5),
                xytext=(0.5, 0.6), textcoords='axes fraction',
                fontsize=20, horizontalalignment='center')
    ax.annotate('Organism Count: %s' % total, xy=(0.5, 0.5),
                xytext=(0.5, 0.5), textcoords='axes fraction',
                fontsize=14, horizontalalignment='center')

    plt.tick_params(labelcolor='none',
                    top=False,
                    bottom=False,
                    left=False,
                    right=False)
    plt.grid(False)

    plt.savefig('images/image_longer_snapshot_%03d.png' % (t))

    print('Saved timestep %s' % (t))
