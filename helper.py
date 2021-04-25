""" helper functions to support main functions"""
import math
import random
import scipy.stats as stats
import variables as const

def generate_random_vector():
    """ to generate random unit vector """
    phi = random.uniform(0.0, math.pi*2)
    theta = math.acos(random.uniform(-1.0, 1.0))

    return math.sin(theta)*math.cos(phi), math.sin(theta)*math.sin(phi),\
        math.cos(theta)

def total_potential_energy(atoms):
    """ function for calculating total potential energy """
    total_energy = 0.0
    for i, atom1 in enumerate(atoms):
        for j, atom2 in enumerate(atoms):
            if j <= i:
                continue

            total_energy += atom1.pair_potent_energy(atom2)

    return total_energy

def print_atoms(atoms, file=None):
    """ A function to print all atoms """
    for each_atom in atoms:
        if file is None:
            print(each_atom)
        else:
            print(each_atom, file=file)

def sample_init_velocities(atoms):
    """ function to sample initial velocities from maxwell-boltzman distribution """
    vel_data = stats.maxwell.rvs(scale=((const.K*const.TEMP)/const.MASS)**0.5 , size=len(atoms) - 1)
    total_vel_x = 0
    total_vel_y = 0
    total_vel_z = 0
    print("velocity DATA:",vel_data)
    for i, atom in enumerate(atoms[1:]):
        x_vec, y_vec, z_vec = generate_random_vector()
        atom.x_vel, atom.y_vel, atom.z_vel = vel_data[i]*x_vec,\
                         vel_data[i]*y_vec, vel_data[i]*z_vec
        total_vel_x += atom.x_vel
        total_vel_y += atom.y_vel
        total_vel_z += atom.z_vel

    atoms[0].x_vel, atoms[0].y_vel, atoms[0].z_vel = -total_vel_x, -total_vel_y, -total_vel_z

    return atoms

def total_force(atom_num, atoms):
    total_force_x, total_force_y, total_force_z = 0.0, 0.0, 0.0
    atom = atoms[atom_num]
    for j, atom2 in enumerate(atoms):
        if atom_num == j:
            continue
        # summing up all the forces
        force_x, force_y, force_z = atom.pair_force(atom2)
        total_force_x += force_x
        total_force_y += force_y
        total_force_z += force_z
    
    return total_force_x, total_force_y, total_force_z
