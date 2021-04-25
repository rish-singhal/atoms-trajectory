""" Module to calculate velocity correlation"""

import matplotlib.pyplot as plt
import math
from tqdm import tqdm

def plot_vel_corr(list_frames):
    """ Function to plot velocity correlation graph """
    mean_values = {}
    size_n = {}

    # To calculate Mean Square Displacement
    for frame1 in tqdm(list_frames):
        for frame2 in list_frames:
            if frame2.time < frame1.time:
                continue

            time_diff = frame2.time - frame1.time
            for atom1, atom2 in zip(frame1.atoms, frame2.atoms):
                mean_values[time_diff] = mean_values.get(time_diff, float(0))
                mean_values[time_diff] += atom1.x_vel * atom2.x_vel +\
	                               atom1.y_vel * atom2.y_vel + atom1.z_vel * atom2.z_vel
                size_n[time_diff] = size_n.get(time_diff, float(0)) + 1

    vcorr_list = []

    for key in mean_values:
        vcorr_list.append(mean_values[key]/size_n[key])

    plt.title("Velocity correlation")
    plt.plot(vcorr_list, color = 'r')
    plt.show()
