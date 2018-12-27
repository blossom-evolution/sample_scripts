from context import blossom

DATASET_OUTPUT_DIR = 'datasets/'

START_TIME = 0
END_TIME = 1

# Create universe
universe = blossom.Universe(world_ds_fn=DATASET_OUTPUT_DIR+'world_ds0.txt',
                            organisms_ds_fn=DATASET_OUTPUT_DIR+'organisms_ds0.txt',
                            current_time=START_TIME,
                            end_time=END_TIME,
                            dataset_dir=DATASET_OUTPUT_DIR,
                            pad_zeroes=0)

# Iterate until end of simulation
universe.run(verbosity=3, expanded=False)
