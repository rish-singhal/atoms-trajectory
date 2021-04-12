""" main file """
from atom import print_atoms
from helper import generate_config, minimize_potential_energy

def main():
    """ main function """
    init_config = generate_config() # generate random config

    with open('init_config.txt', 'w') as f:
        # printing inital configuration
        print("Initial Configuration:\n-------------\n", file=f)
        print_atoms(init_config, file=f)

    final_config = minimize_potential_energy(init_config)

    with open('min_config.txt', 'w') as f:
        # printing inital configuration
        print("Configuration after minimizing potential energy:\n-------------\n", file=f)
        print_atoms(final_config, file=f)

if __name__ == "__main__":
    main()
