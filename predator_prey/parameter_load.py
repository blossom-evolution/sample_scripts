from context import blossom

import world_params
import predator_params
import prey_params

DATASET_OUTPUT_DIR = 'datasets'

START_TIME = 0
END_TIME = 999

# Create universe
universe = blossom.Universe(world_param_dict=world_params.world_dict,
                            species_param_dicts=[predator_params.species_dict,
                                                 prey_params.species_dict],
                            current_time=START_TIME,
                            end_time=END_TIME,
                            dataset_dir=DATASET_OUTPUT_DIR,
                            pad_zeros=4,
                            seed=42)

# Iterate until end of simulation
universe.run(verbosity=4, expanded=False)
