""" Atom class """
import variables as const

class Atom:
    """ class for representing an atom """
    def __init__(self, x_cor, y_cor, z_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.z_cor = z_cor
        self.x_vel = 0.0
        self.y_vel = 0.0
        self.z_vel = 0.0

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

    def apply_pbcondition2(self):
        """ for changing position of the particle from left  to right """
        if self.x_cor > const.LEN:
            self.x_cor = self.x_cor - const.LEN
        elif self.x_cor < 0:
            self.x_cor = self.x_cor + const.LEN

        if self.y_cor > const.LEN:
            self.y_cor = self.y_cor - const.LEN
        elif self.y_cor < 0:
            self.y_cor = self.y_cor + const.LEN

        if self.z_cor > const.LEN:
            self.z_cor = self.z_cor - const.LEN
        elif self.z_cor < 0:
            self.z_cor = self.z_cor + const.LEN

    def __str__(self):
        return "Ar "+str(self.x_cor)+" "+str(self.y_cor)+" "\
        	    +str(self.z_cor)
