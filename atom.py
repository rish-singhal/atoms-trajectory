""" Atom class """
import constants as const

class Atom:
    """ class for representing an atom """
    def __init__(self, x_cor, y_cor, z_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.z_cor = z_cor

    def distance_sq(self, atom2):
        """ for calculating square distance between two atoms """
        return (self.x_cor - atom2.x_cor)**2\
             + (self.y_cor - atom2.y_cor)**2\
             + (self.z_cor - atom2.z_cor)**2

    def pair_potent_energy(self, atom2):
        """ for calculating pair potential energy """
        distance = self.distance_sq(atom2)**0.5
        return 4*const.EPSILON*((const.SIGMA/distance)**12\
            - (const.SIGMA/distance)**6)

    def pair_force(self, atom2):
        """ returns force vector between a pair """
        force_x = self.x_cor - atom2.x_cor
        force_y = self.y_cor - atom2.y_cor
        force_z = self.z_cor - atom2.z_cor
        distance = self.distance_sq(atom2)**0.5
        factor = (24*const.EPSILON/(distance**2))*(2*((const.SIGMA\
            /distance)**12) - (const.SIGMA/distance)**6)

        return force_x*factor, force_y*factor, force_z*factor

    def apply_pbcondition(self):
        """ for applying periodic boundary condition, such that atom remains in the box """
        self.x_cor = max(0.0, min(const.LEN, self.x_cor))
        self.y_cor = max(0.0, min(const.LEN, self.y_cor))
        self.z_cor = max(0.0, min(const.LEN, self.z_cor))

    def __str__(self):
        return "Ar "+str(self.x_cor)+" "+str(self.y_cor)+" "\
        	    +str(self.z_cor)

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
