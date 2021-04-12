""" helper functions """
import random
from atom import Atom, total_potential_energy
import constants as const

def generate_config():
    """ generating initial configuration """

    atoms = [] # List of atoms
    # generate 108 atoms with distance constraints
    for _ in range(const.N):
        # randomly generate coordinates till it satisfy
        #		distance constraints
        while True:
            x_cor = random.uniform(0.0, const.LEN)
            y_cor = random.uniform(0.0, const.LEN)
            z_cor = random.uniform(0.0, const.LEN)
            new_atom = Atom(x_cor, y_cor, z_cor)

            check = 1
            for atom in atoms:
        	    # enforcing distance constraint
                if (atom.distance_sq(new_atom))**0.5 < const.MIN_DIST:
                    check = 0
                    break

            if check:
                atoms.append(new_atom)
                break

    return atoms

def minimize_potential_energy(atoms):
    # print initial total potential energy
    print("-------------")
    print("initial potential energy:", round(total_potential_energy(atoms), 5), "kcal/mol")
    print("-------------\n")
