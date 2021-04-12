""" main file """
from atom import print_atoms
from helper import generate_config

def main():
    """ main function """
    init_atoms = generate_config() # generate random config

    # printing inital configuration
    print("Initial Configuration:\n-------------\n")
    print_atoms(init_atoms)

if __name__ == "__main__":
    main()
