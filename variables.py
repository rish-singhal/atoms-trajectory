""" constants """

# TODO: Update constant config

N = 108 # Number of atoms
LEN = 18.0 # Angstrom
EPSILON = 0.238 # 0.238 kcal/mol
SIGMA = 3.4 # Angstrom
MIN_DIST = 3.4 # Angstrom

# For gradient descent
DELTA = 0.001 # energy difference to break gradient descent
ETA = 0.1 # learning rate

# For trajectory generation
# TODO : update to take it as input
# TODO : update Mass of Argon
ITERATIONS = 1000
TIME_STEP = 4 # 4 femto seconds
MASS = 1 # mass of Argon

#For Sampeling velocities
K = 1 # Boltzman Constant
TEMP = 300 # Temperature = 300 Kelvin


# N = 108 # Number of atoms
# LEN = 18e-10 # Angstrom
# EPSILON = 1.66e-21 # 0.238 kcal/mol
# SIGMA = 3.4e-10 # Angstrom
# MIN_DIST = 3.4e-10 # Angstrom

# # For gradient descent
# DELTA = 0.001 # energy difference to break gradient descent
# ETA = 0.1 # learning rate

# # For trajectory generation
# # TODO : update to take it as input
# # TODO : update Mass of Argon
# ITERATIONS = 1000
# TIME_STEP = 4 # 4 femto seconds
# MASS = 6.633359936e-26 # mass of Argon (in Kg)

# #For Sampeling velocities
# K = 1.38e-10 # Boltzman Constant
# TEMP = 300 # Temperature = 300 Kelvin
