# This is the parameter file for a species of organism.
import math

species_dict = {}

# Identifier (str)
species_dict['species_name'] = 'predator1'

# Number of organisms (int)
species_dict['population_size'] = 10

# Initial DNA length (int)
species_dict['dna_length'] = 4

# Maximum old age (int, or 'None')
species_dict['max_age'] = math.inf

# Action specification (str)
species_dict['action_type'] = 'predator'

# Movement specification (str)
species_dict['movement_type'] = 'stationary'

# Reproduction specification (str)
species_dict['reproduction_type'] = 'pure_replication'

# male, female, asexual, hermaphrodite
species_dict['proportion_m'] = 0.5
species_dict['proportion_f'] = 0.5
species_dict['proportion_a'] = 0.0
species_dict['proportion_h'] = 0.0

# Water intake method (str, or 'None')
species_dict['drinking_type'] = None

# Water capacity (int, or 'None')
species_dict['water_capacity'] = 40

# Initial water level (int, or 'None')
species_dict['water_initial'] = 20

# Water metabolism, in water per integer timestep (int, or 'None')
species_dict['water_metabolism'] = 2

# Water intake, in food per integer timestep (int, or 'None')
species_dict['water_intake'] = 4

# Lifetime without water (int, or 'None')
species_dict['max_time_without_water'] = 2

# Food intake method (str, or 'None')
species_dict['eating_type'] = 'eat_prey1'

# Food capacity (int, or 'None')
species_dict['food_capacity'] = 50

# Initial food level (int, or 'None')
species_dict['food_initial'] = 50

# Food metabolism, in food per integer timestep (int, or 'None')
species_dict['food_metabolism'] = 1

# Food intake, in food per integer timestep (int, or 'None')
species_dict['food_intake'] = 8

# Lifetime without food (int, or 'None')
species_dict['max_time_without_food'] = 5

# Whether organisms can mutate (bool)
species_dict['can_mutate'] = False

# Mutation rate, in bit flips per integer timestep (int, or 'None')
species_dict['mutation_rate'] = None

# File path for custom methods, if any
species_dict['custom_module_fns'] = ['predator_action.py',
                                     'predator_eating.py']

# Initial positions for each organisms (must be list of lists)
# species_dict['initial_positions'] = [
#     [0, 0],
#     [2, 2],
#     [4, 4],
#     [6, 6],
# ]

species_dict['initial_positions'] = [[0, 0]] * species_dict['population_size']
