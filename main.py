""" main file """
import helper 
from functions import generate_config, minimize_potential_energy,\
            generate_frames
from msd import plot_MSD
from vanhove import plot_van_hove
from velcorr import plot_vel_corr
from dynamic_factor import plot_dynamic_factor
from copy import deepcopy
import pickle
import numpy as np
import os, fnmatch



def main():
    """ main function """
    frames = []
    ITERATIONS = 0
    while(True):

        print(">> ", end="")

        inp = input()

        
        if inp == "help":
            print("ls: Print the file names in the current directory")
            print("gen ITERATIONS: Generate ITERATIONS and save in file")
            print("load INPUT_FILE: Provide Input File")
            print("load vanhove INPUT_FILE: Provide Input File")
            print("plot msd: Plot Mean Square Displacement")
            print("plot vanhove: Plot Van Hove Correlation")
            print("plot vel: Plot Velocity Correlation")
            print("plot df: Plot Dynamic Factor")
            print("exit: EXIT")

        elif inp == "ls":
            listOfFiles = os.listdir('.')
            pattern = "*.pkl"
            for entry in listOfFiles:
                if fnmatch.fnmatch(entry, pattern):
                    print(entry)


        elif inp[0:3] == "gen":
            try:
                ITERATIONS = int(inp.split()[1])
            except:
                print("Provide the numeber of iterations!")
                continue

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

            frames = generate_frames(deepcopy(final_config_vel), ITERATIONS)

            print("Recieved Frames")

            with open('frames_'+str(ITERATIONS) +'.pkl', 'wb') as f:
                pickle.dump(frames, f)

            helper.plot_rij(init_config)

        elif inp[0:12] == "load vanhove":
            try:
                file_name = inp.split()[2] 
            except:
                print("Provide File Name!")
                continue
            
            try:
                with open(file_name, 'rb') as f:
                    van_hove = pickle.load(f)
            except:
                print("File does not exist.")
                continue

        elif inp[0:4] == "load":
            try:
                file_name = inp.split()[1] 
            except:
                print("Provide File Name!")
                continue
            try:
                with open(file_name, 'rb') as f:
                    frames = pickle.load(f)
            except:
                print("File does not exist.")
                continue


            print("Loaded", file_name)

        elif inp == "plot msd":
            if len(frames) == 0:
                print("Either generate frames or give a file as input")
                continue
            plot_MSD(frames)

        elif inp == "plot vanhove":
            if len(frames) == 0:
                print("Either generate frames or give a file as input")
                continue
            
            van_hove = plot_van_hove(frames)
            with open('van_hove_'+str(len(frames))+'.pkl', 'wb') as f:
                pickle.dump(van_hove, f)

        elif inp == "plot vel":
            if len(frames) == 0:
                print("Either generate frames or give a file as input")
                continue
            plot_vel_corr(frames)

        elif inp == "plot df":
            if len(van_hove) == 0:
                print("Execute Van Hove first or load van_hove file.")
                continue
            
            plot_dynamic_factor(van_hove)


        elif inp == "exit":
            break

        else:
            print("Enter 'help' command for instructions")

    # # function to plot Mean Square Displacement
    # # function to plot Van Hove Correlation Function
    #plot_vel_corr(frames) # function to plot Velocity Correlation Function
    

    

if __name__ == "__main__":
    main()
