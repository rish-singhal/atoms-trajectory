""" Function to calculate Mean Square Displacement """
import matplotlib.pyplot as plt
import atom
import frame
import numpy as np
from tqdm import tqdm

def plot_MSD(list_frames): 
    """ To calculate Mean Square Displacement """
    len_frames = len(list_frames)
    mean_values = np.zeros(len_frames)
    size_n = np.zeros(len_frames)

    for frame1 in tqdm(list_frames):
        for frame2 in list_frames:
            if frame2.time <= frame1.time:
                continue
            
            time_diff = frame2.time - frame1.time
            for atom1, atom2 in zip(frame1.atoms, frame2.atoms):
                #print("distance", atom1.x_cor, atom2.x_cor, (atom1.x_cor - atom2.x_cor)**2)
                mean_values[time_diff] += atom1.distance_sq(atom2)
                size_n[time_diff] += 1

    np.seterr(divide='ignore', invalid='ignore')
    msd_list = np.divide(mean_values, size_n)

    # Diffusion Constant
    #value = (msd_list[::-1] - msd_list[::-50])/(50.0*6)

    #print("Diffusion Constant: " + str(value))

    #print(msd_list)
    plt.title("Mean Square Displacement")
    plt.plot(msd_list, color = 'r')
    plt.show()
