""" Module to plot van hove correlation """

import matplotlib.pyplot as plt
import math
import numpy as np
from tqdm import tqdm

def plot_van_hove(list_frames, van_hove_pkl = None):
	""" function to plot van hove correlation """
	
	if van_hove_pkl is not None:
		van_hove = van_hove_pkl
		max_time_diff = 300
	else:
		max_time_diff = len(list_frames)
		
		# max_distance = 32 Angstrom
		mean_values = np.zeros((max_time_diff, 40))

		# To calculate Van Hove Displacement Graph
		for frame1 in tqdm(list_frames):
			for time_diff in range(max_time_diff - frame1.time):
				frame2 = list_frames[frame1.time + time_diff]

				for atom1 in frame1.atoms:
					for atom2 in frame2.atoms:
						r = int(round((atom1.distance_sq(atom2)**0.5)*(10**10), 0))
						mean_values[time_diff][r] += 1

		van_hove = mean_values/mean_values.sum(axis=1)[:,None]

	if max_time_diff < 250:
		plt.plot(van_hove[0], color = 'r')
		plt.plot(van_hove[10], color = 'g')
		plt.plot(van_hove[20], color = 'y')
		plt.plot(van_hove[40], color = 'b')

		plt.title("Van Hove correlation")
		plt.legend(["t = 0", "t = 10", "t = 20", "t = 40"])
		plt.show()

	elif max_time_diff >= 250:
		plt.plot(van_hove[0], color = 'r')
		plt.plot(van_hove[50], color = 'g')
		plt.plot(van_hove[100], color = 'y')
		plt.plot(van_hove[200], color = 'b')

		plt.title("Van Hove correlation")
		plt.legend(["t = 0", "t = 50", "t = 100", "t = 200"])
		plt.show()

	return van_hove
