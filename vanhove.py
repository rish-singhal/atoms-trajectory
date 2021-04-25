""" Module to plot van hove correlation """

import matplotlib.pyplot as plt
import math
import numpy as np

def plot_van_hove(list_frames):
	""" function to plot van hove correlation """
	max_time_diff = len(list_frames)
	
	# max_distance = 32 Angstrom
	mean_values = np.zeros((max_time_diff, 40))

	# To calculate Van Hove Displacement Graph
	for frame1 in list_frames:
		for frame2 in list_frames:
			if frame2.time < frame1.time:
				continue

			time_diff = frame2.time - frame1.time

			for atom1 in frame1.atoms:
				for atom2 in frame2.atoms:
					r = int(round((atom1.distance_sq(atom2)**0.5)*(10**10), 0))
					mean_values[time_diff][r] += 1

	van_hove = mean_values/mean_values.sum(axis=1)[:,None]



	plt.plot(van_hove[0], color = 'r')
	plt.plot(van_hove[30], color = 'g')
	plt.plot(van_hove[100], color = 'y')
	plt.plot(van_hove[250], color = 'b')

	plt.title("Van Hove correlation")
	plt.legend(["t = 0", "t = 30", "t = 100", "t = 250"])
	plt.show()

	return van_hove
