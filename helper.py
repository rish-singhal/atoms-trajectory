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
    """ to minimize potential energy via gradient descent """
    # print initial total potential energy
    print("Starting Gradient Descent....")

    prev_potential_energy = total_potential_energy(atoms)

    print("-------------")
    print("initial potential energy:", round(prev_potential_energy, 5), "kcal/mol")
    print("-------------\n")

    iteration = 1
    # performing gradient descent
    while True:
        for i, atom in enumerate(atoms):
            # initializing total force on ith atom
            total_force_x, total_force_y, total_force_z = 0.0, 0.0, 0.0
            for j, atom2 in enumerate(atoms):
                if i == j:
                    continue
                # summing up all the forces
                force_x, force_y, force_z = atom.pair_force(atom2)
                total_force_x += force_x
                total_force_y += force_y
                total_force_z += force_z

            # updating cordinates according to descent equation
            atom.x_cor += const.ETA*total_force_x
            atom.y_cor += const.ETA*total_force_y
            atom.z_cor += const.ETA*total_force_z

            atom.apply_pbcondition()

        # calculating updated potential energy
        new_potential_energy = total_potential_energy(atoms)

        print("Interation", iteration)
        print("-------------")
        print("potential energy:", round(new_potential_energy, 5), "kcal/mol")
        print("-------------\n")

        if abs(prev_potential_energy - new_potential_energy) < const.DELTA:
            print("Diff:", new_potential_energy - prev_potential_energy)
            print("Ending gradient descent as difference it is less than DELTA")
            break

        # update iteration value, prev_potential_energy
        iteration += 1
        prev_potential_energy = new_potential_energy

    return atoms
