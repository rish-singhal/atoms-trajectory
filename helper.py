""" helper functions """
import random
from atom import Atom
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

def total_potential_energy(atoms):
    """ function for calculating total potential energy """
    total_energy = 0.0
    for i, atom1 in enumerate(atoms):
        for j, atom2 in enumerate(atoms):
            if j <= i: continue

            total_energy += atom1.pair_potential_energy(atom2)

    return total_energy



def minimize_potential_energy(atoms):
