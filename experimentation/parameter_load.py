from context import blossom

WORLD_FN = None
ORGANISMS_FN = None
WORLD_PARAM_FN = 'world.param'
SPECIES_PARAM_FNS = ['species1.param']
CUSTOM_METHODS_FNS = ['custom_methods.py']
DATASET_OUTPUT_DIR = 'datasets/longer/'

START_TIME = 0
END_TIME = 100

# Create universe
universe = blossom.Universe(world_ds_fn=WORLD_FN,
                            organisms_ds_fn=ORGANISMS_FN,
                            world_param_fn=WORLD_PARAM_FN,
                            species_param_fns=SPECIES_PARAM_FNS,
                            custom_methods_fns=CUSTOM_METHODS_FNS,
                            current_time=START_TIME,
                            end_time=END_TIME,
                            dataset_dir=DATASET_OUTPUT_DIR)

print('t = %s: %s organisms' % (universe.current_time,
                                len(universe.organism_list)))

# Iterate until end of simulation
while universe.current_time < universe.end_time:
    universe.step()
    print('t = %s: %s organisms' % (universe.current_time,
                                    len(universe.organism_list)))
