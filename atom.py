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

def print_atoms(atoms, f=None):
    """ A function to print all atoms """
    for each_atom in atoms:
        if f == None:
            print(each_atom)
        else:
            print(each_atom, file=f)

