""" constants """

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
ITERATIONS = 1,000
TIME_STEP = 4 # 4 femto seconds
MASS = 1 # mass of Argon
