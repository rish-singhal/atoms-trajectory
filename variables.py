""" constants """

N = 108 # Number of atoms
LEN = float(18*(10**-10)) # Angstrom
EPSILON = float(1.66*(10**-21)) # 0.238 kcal/mol
SIGMA = float(3.4*(10**-10)) # Angstrom
MIN_DIST = float(3.4*(10**-10)) # Angstrom

# For gradient descent
DELTA = 0.01 # energy difference to break gradient descent
ETA = 0.1 # learning rate

# For trajectory generation
ITERATIONS = 300
TIME_STEP = float(4*(10**-15)) # 4 femto seconds
MASS = float(6.633359936*(10**-26)) # mass of Argon (in Kg)

#For Sampeling velocities
K = float(1.38*(10**-23)) # Boltzman Constant
TEMP = 300 # Temperature = 300 Kelvin
