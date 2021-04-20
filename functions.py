""" main functions """
import random
from atom import Atom
from frame import Frame
import variables as const
import helper
import copy
from copy import deepcopy

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

    prev_potential_energy = helper.total_potential_energy(atoms)

    print("-------------")
    print("initial potential energy:", round(prev_potential_energy, 5), "kcal/mol")
    print("-------------\n")

    iteration = 1
    # performing gradient descent
    while True:
        for i, atom in enumerate(atoms):
            # initializing total force on ith atom
            total_force_x, total_force_y, total_force_z = helper.total_force(i, atoms)

            # updating cordinates according to descent equation
            atom.x_cor += const.ETA*total_force_x
            atom.y_cor += const.ETA*total_force_y
            atom.z_cor += const.ETA*total_force_z

            atom.apply_pbcondition()

        # calculating updated potential energy
        new_potential_energy = helper.total_potential_energy(atoms)

        print("Interation", iteration)
        print("-------------")
        print("potential energy:", round(new_potential_energy, 5), "kcal/mol")
        print("-------------\n")

        if abs(prev_potential_energy - new_potential_energy) < const.DELTA:
            print("Diff:", new_potential_energy - prev_potential_energy)
            print("Ending gradient descent as difference is less than DELTA =", const.DELTA)
            break

        # update iteration value, prev_potential_energy
        iteration += 1
        prev_potential_energy = new_potential_energy

    return atoms

def generate_frames(atoms):
    frames = []
    frames.append(Frame(atoms, 0))
    prev_frame = copy.deepcopy(atoms)

    # for atom in atoms:
    #     print(atom.x_cor, atom.y_cor, atom.z_cor)

    for num in range(const.ITERATIONS - 1):
        new_frame = copy.deepcopy(prev_frame)
        old_force_x = list()
        old_force_y = list()
        old_force_z = list()
        
        for i, atom in enumerate(prev_frame):
            # initializing total force on ith atom
            total_force_x, total_force_y, total_force_z = helper.total_force(i, prev_frame)

            # update positions
            #print(new_frame[i].x_cor, prev_frame[i].x_cor, "first")
            new_frame[i].x_cor = prev_frame[i].x_cor + prev_frame[i].x_vel*const.TIME_STEP\
                         + (total_force_x/(2*const.MASS))*(const.TIME_STEP**2)
            new_frame[i].y_cor = prev_frame[i].y_cor + prev_frame[i].y_vel*const.TIME_STEP\
                         + (total_force_y/(2*const.MASS))*(const.TIME_STEP**2)
            new_frame[i].z_cor = prev_frame[i].z_cor + prev_frame[i].z_vel*const.TIME_STEP\
                         + (total_force_z/(2*const.MASS))*(const.TIME_STEP**2)

            
            #print("diii", new_frame[i].x_cor, prev_frame[i].x_cor + prev_frame[i].z_vel*const.TIME_STEP + (total_force_x/(2*const.MASS))*(const.TIME_STEP**2))
            # applying periodic boundary condition
            new_frame[i].apply_pbcondition2()
            #print(new_frame[i].x_cor, prev_frame[i].x_cor, "second")
            print(new_frame[i].x_cor, prev_frame[i].x_cor, "frames")

            old_force_x.append(total_force_x)
            old_force_y.append(total_force_y)
            old_force_z.append(total_force_z)
        
        for i, atom in enumerate(prev_frame):
            # initializing total force on ith atom
            total_force_x, total_force_y, total_force_z = helper.total_force(i, new_frame)

            # update velocities
            new_frame[i].x_vel = prev_frame[i].x_vel +\
                         + ((old_force_x[i] + total_force_x)/(2*const.MASS))*(const.TIME_STEP)
            new_frame[i].y_vel = prev_frame[i].y_vel +\
                         + ((old_force_y[i] + total_force_y)/(2*const.MASS))*(const.TIME_STEP)
            new_frame[i].z_vel = prev_frame[i].z_vel +\
                         + ((old_force_z[i] + total_force_z)/(2*const.MASS))*(const.TIME_STEP)

        frames.append(Frame(new_frame, num+1))
        prev_frame = copy.deepcopy(new_frame)

    # for atom1, atom2 in zip(frames[0].atoms, frames[1].atoms):
    #     print(atom1.x_cor, atom2.x_cor, "dii")

    return frames
