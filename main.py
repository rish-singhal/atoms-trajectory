""" main file """
import helper 
from functions import generate_config, minimize_potential_energy,\
            generate_frames
from msd import plot_MSD
from vanhove import plot_van_hove
from velcorr import plot_vel_corr
from copy import deepcopy

def main():
    """ main function """
    init_config = generate_config() # generate random config

    with open('init_config.txt', 'w') as f:
        # printing inital configuration
        print("Initial Configuration:\n-------------\n", file=f)
        helper.print_atoms(deepcopy(init_config), file=f)
    
    # plot_histogram(init_config)

    final_config = minimize_potential_energy(deepcopy(init_config))

    with open('min_config.txt', 'w') as f:
        # printing inital configuration
        print("Configuration after minimizing potential energy:\n-------------\n", file=f)
        helper.print_atoms(deepcopy(final_config), file=f)

    final_config_vel = helper.sample_init_velocities(deepcopy(final_config))

    frames = generate_frames(deepcopy(final_config_vel))

    print("Recieved Frames")

    plot_MSD(deepcopy(frames)) # function to plot Mean Square Displacement
    plot_van_hove(deepcopy(frames)) # function to plot Van Hove Correlation Function
    plot_vel_corr(deepcopy(frames)) # function to plot Velocity Correlation Function

if __name__ == "__main__":
    main()
