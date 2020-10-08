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

import blossom
import flowerpot


time = 999
DATASET_OUTPUT_DIR = 'datasets'
IMAGE_OUTPUT_DIR = 'images'

plot_dicts = {'predator1': [], 'prey1': []}

ts = flowerpot.TimeSeries(DATASET_OUTPUT_DIR)

# for ds in ts:
#     population_dict = ds.population_dict
#     for species in population_dict:
#         plot_dicts[species].append(population_dict[species]['statistics']['alive'])


def alive_count(species):
    return lambda ds: ds.population_dict[species]['statistics']['alive']


fig = plt.figure(figsize=(10, 8))

ts.plot_ts([
    ('predator1', alive_count('predator1')),
    ('prey1', alive_count('prey1'))
])




# plt.plot(plot_dicts['predator1'], 'r', label='predators')
# plt.plot(plot_dicts['prey1'], 'b', label='prey')
# plt.plot([0] * len(plot_dicts['prey1']), 'k--')

# plt.xlabel('Timestep')
# plt.ylabel('Population Count')
# plt.legend()

plt.savefig('%s/populations_plot.pdf' % (IMAGE_OUTPUT_DIR))
