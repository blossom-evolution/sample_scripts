from context import blossom

import world_params
import species1_params

DATASET_OUTPUT_DIR = 'datasets/custom_positions/'

START_TIME = 0
END_TIME = 10

# Create universe
universe = blossom.Universe(world_param_dict=world_params.world_dict,
                            species_param_dicts=[species1_params.species_dict],
                            current_time=START_TIME,
                            end_time=END_TIME,
                            dataset_dir=DATASET_OUTPUT_DIR)

# Iterate until end of simulation
universe.run(verbosity=3, expanded=False)
