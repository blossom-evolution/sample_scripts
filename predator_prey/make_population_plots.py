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
    for i in range(time + 1):
        try:
            with open(organism_paths[i], 'r') as f:
                population_dict = json.load(f)
            plot_dicts[species].append(population_dict[species]['statistics']['alive_count'])
        except:
            pass

fig = plt.figure(figsize=(10, 8))

plt.plot(plot_dicts['predator1'], 'r', label='predators')
plt.plot(plot_dicts['prey1'], 'b', label='prey')
plt.plot([0] * len(plot_dicts['prey1']), 'k--')

plt.xlabel('Timestep')
plt.ylabel('Population Count')
plt.legend()

plt.savefig('%s/populations_plot.pdf' % (IMAGE_OUTPUT_DIR))
