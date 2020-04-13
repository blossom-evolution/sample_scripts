import os
import sys
import errno
import glob
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/blossom')
sys.path.append('/Users/bryanbrzycki/Documents/Personal/Evolution-Code/Code/flowerpot')

import json

import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

time = 999
DATASET_OUTPUT_DIR = 'datasets'
IMAGE_OUTPUT_DIR = 'images'

organism_paths = sorted(glob.glob('%s/organisms_ds???.txt'
                                  % DATASET_OUTPUT_DIR))[:(time + 1)]
world_paths = sorted(glob.glob('%s/world_ds???.txt' % DATASET_OUTPUT_DIR))[:(time + 1)]

try:
    os.makedirs(IMAGE_OUTPUT_DIR)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

with open(world_paths[0], 'r') as f:
    world = json.load(f)

timesteps = list(range(time + 1))
world_size = world['world_size']

maxes = []
plot_dicts = {'predator1': [], 'prey1': []}

for species in ['predator1', 'prey1']:
    max_val = 0

    for i in range(time + 1):

        living_organisms = 0

        plot = [[0 for x in range(world_size[1])]
                for x in range(world_size[0])]

        with open(organism_paths[i], 'r') as f:
            organism_list = json.load(f)

        for organism in organism_list:
            if organism['alive'] and organism['species_name'] == species:
                plot[organism['position'][0]][organism['position'][1]] += 1
                living_organisms += 1

        plot_dicts[species].append(living_organisms)

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

    with open(organism_path, 'r') as f:
        organism_list = json.load(f)
    with open(world_path, 'r') as f:
        world = json.load(f)

    world_size = world['world_size']
    predators = [[0 for x in range(world_size[1])] for x in range(world_size[0])]
    prey = [[0 for x in range(world_size[1])] for x in range(world_size[0])]

    predator_total = 0
    prey_total = 0
    for organism in organism_list:
        if organism['alive']:
            if organism['species_name'] == 'predator1':
                predators[organism['position'][0]][organism['position'][1]] += 1
                predator_total += 1
            else:
                prey[organism['position'][0]][organism['position'][1]] += 1
                prey_total += 1
            total += 1

    fig = plt.figure(constrained_layout=True, figsize=(10, 10))
    gs = gridspec.GridSpec(ncols=4, nrows=4, figure=fig)

    ax0 = fig.add_subplot(gs[0:2, 0:2], frameon=False)
    plt.sca(ax0)

    plt.annotate('Timestep: %03d' % t, xy=(0.5, 0.5),
                 xytext=(0.5, 0.6), textcoords='axes fraction',
                 fontsize=20, horizontalalignment='center')
    plt.annotate('Organism Count: %s' % total, xy=(0.5, 0.5),
                 xytext=(0.5, 0.5), textcoords='axes fraction',
                 fontsize=14, horizontalalignment='center')

    plt.annotate('Predators: %05d' % predator_total, xy=(0.5, 0.5),
                 xytext=(0.5, 0.35), textcoords='axes fraction',
                 fontsize=12, horizontalalignment='center')
    plt.annotate('Prey:      %05d' % prey_total, xy=(0.5, 0.5),
                 xytext=(0.5, 0.3), textcoords='axes fraction',
                 fontsize=12, horizontalalignment='center')

    plt.tick_params(labelcolor='none',
                    top=False,
                    bottom=False,
                    left=False,
                    right=False)
    plt.grid(False)

    ax1 = fig.add_subplot(gs[0:2, 2:4])
    plt.sca(ax1)

    plt.plot(plot_dicts['predator1'], 'r', label='predators')
    plt.plot(plot_dicts['prey1'], 'b', label='prey')
    plt.plot([0] * len(plot_dicts['prey1']), 'k--')
    plt.axvline(x=t, linestyle='--')
    plt.plot(t, plot_dicts['predator1'][t], 'bo')
    plt.plot(t, plot_dicts['prey1'][t], 'ro')

    plt.xlabel('Timestep')
    plt.ylabel('Population Count')
    plt.legend()

    ax2 = fig.add_subplot(gs[2:4, 0:2])
    plt.sca(ax2)

    plt.imshow(predators)
    plt.title('Predators')
    plt.clim(0, maxes[0])
    plt.colorbar()

    ax3 = fig.add_subplot(gs[2:4, 2:4])
    plt.sca(ax3)

    plt.imshow(prey)
    plt.title('Prey')
    plt.clim(0, maxes[1])
    plt.colorbar()

    plt.savefig('%s/image_snapshot_%03d.png' % (IMAGE_OUTPUT_DIR, t))

    print('Saved timestep %s' % (t))
