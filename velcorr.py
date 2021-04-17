""" Module to calculate velocity correlation"""

import matplotlib.pyplot as plt
import math


def plot_vel_corr(list_frames):
	""" Function to plot velocity correlation graph """
	mean_values = {}
	size_n = {}

	# To calculate Mean Square Displacement
	for frame1 in list_frames:
		for frame2 in list_frames:
			if frame2.time < frame1.time:
				continue

			time_diff = frame2.time - frame1.time
			for atom1, atom2 in zip(frame1.atoms, frame2.atoms):
				mean_values[time_diff] = mean_values.get(time_diff, 0)
	            mean_values[time_diff] += atom1.vel_x * atom2.vel_x +\
	                        			atom1.vel_y * atom2.vel_y + atom1.vel_z * atom2.vel_z
	            size_n[time_diff] = size_n(time_diff, 0) + 1

	vcorr_list = []

	for key in mean_values:
		vcorr_list.append(mean_values[key]/size_n[key])

	plt.plot(vcorr_list, color = 'r')
	plt.show()
