""" constants """

# TODO: Update constant config

# N = 108 # Number of atoms
# LEN = 18.0 # Angstrom
# EPSILON = 0.238 # 0.238 kcal/mol
# SIGMA = 3.4 # Angstrom
# MIN_DIST = 3.4 # Angstrom

# # For gradient descent
# DELTA = 0.001 # energy difference to break gradient descent
# ETA = 0.1 # learning rate

# # For trajectory generation
# # TODO : update to take it as input
# # TODO : update Mass of Argon
# ITERATIONS = 300
# TIME_STEP = 4e-15 # 4 femto seconds
# MASS = 6.633359936e-26 # mass of Argon

# #For Sampeling velocities
# K = 1.38e-10 # Boltzman Constant
# TEMP = 300 # Temperature = 300 Kelvin


N = 108 # Number of atoms
LEN = float(18*(10**-10)) # Angstrom
EPSILON = float(1.66*(10**-21)) # 0.238 kcal/mol
SIGMA = float(3.4*(10**-10)) # Angstrom
MIN_DIST = float(3.4*(10**-10)) # Angstrom

# For gradient descent
DELTA = 0.01 # energy difference to break gradient descent
ETA = 0.1 # learning rate

# For trajectory generation
# TODO : update to take it as input
# TODO : update Mass of Argon
ITERATIONS = 300
TIME_STEP = float(4*(10**-15)) # 4 femto seconds
MASS = float(6.633359936*(10**-26)) # mass of Argon (in Kg)

#For Sampeling velocities
K = float(1.38*(10**-23)) # Boltzman Constant
TEMP = 300 # Temperature = 300 Kelvin
