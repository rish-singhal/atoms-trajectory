""" Module to plot dynamic structure factor """

import matplotlib.pyplot as plt
import math
import numpy as np
import pickle

def plot_dynamic_factor(van_hove):
	""" function to plot dynamic structure factor """

	distance_F_k_t = np.array([np.fft.fft(row) for row in van_hove]).T
	dynamic_factor_k_w = np.array([np.fft.fft(row) for row in distance_F_k_t])

	plt.plot(dynamic_factor_k_w[1], color = 'r')
	plt.plot(dynamic_factor_k_w[2], color = 'g')
	plt.plot(dynamic_factor_k_w[3], color = 'y')
	plt.plot(dynamic_factor_k_w[4], color = 'b')

	plt.title("Dynamic Structure Factor")
	plt.legend(["w = 1", "w = 2", "w = 3", "w = 5"])
	plt.show()



