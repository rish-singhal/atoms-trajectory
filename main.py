""" main file """
import helper 
from functions import generate_config, minimize_potential_energy,\
            generate_frames
from msd import plot_MSD
from vanhove import plot_van_hove
from velcorr import plot_vel_corr

def main():
    """ main function """
    init_config = generate_config() # generate random config

    with open('init_config.txt', 'w') as f:
        # printing inital configuration
        print("Initial Configuration:\n-------------\n", file=f)
        helper.print_atoms(init_config, file=f)

    final_config = minimize_potential_energy(init_config)

    with open('min_config.txt', 'w') as f:
        # printing inital configuration
        print("Configuration after minimizing potential energy:\n-------------\n", file=f)
        helper.print_atoms(final_config, file=f)

    final_config_vel = helper.sample_init_velocities(final_config)

    frames = generate_frames(final_config_vel)

    plot_MSD(frames) # function to plot Mean Square Displacement
    plot_van_hove(frames) # function to plot Van Hove Correlation Function
    plot_vel_corr(frames) # function to plot Velocity Correlation Function

if __name__ == "__main__":
    main()
