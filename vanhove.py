""" Module to plot van hove correlation """

import matplotlib.pyplot as plt
import math

def plot_van_hove(list_frames):
	""" function to plot van hove correlation """
	mean_values_1 = {}
	mean_values_30 = {}
	mean_values_100 = {}
	mean_values_250 = {}
	size_n = {0 : 0, 50: 0, 100: 0, 30 : 0, 250: 0}

	# To calculate Van Hove Displacement Graph
	for frame1 in list_frames:
		for frame2 in list_frames:
			if frame2.time < frame1.time:
				continue

			time_diff = frame2.time - frame1.time

			# if time_diff != 250:
			# 	continue

			if time_diff == 0 or time_diff == 30 or time_diff == 100 or time_diff == 250:
				ans = 1
			else:
				continue


			for atom1 in frame1.atoms:
				for atom2 in frame2.atoms:
							if time_diff == 0:
								r = math.sqrt(atom1.distance_sq(atom2))
								if not mean_values_1.get(r):
									mean_values_1[r] = 0.0
								mean_values_1[r] += 1 
								size_n[time_diff] += 1

							if time_diff == 30:
								r = math.sqrt(atom1.distance_sq(atom2))
								if not mean_values_30.get(r):
									mean_values_30[r] = 0.0
								mean_values_30[r] += 1 
								size_n[time_diff] += 1

							if time_diff == 100:
								r = math.sqrt(atom1.distance_sq(atom2))
								if not mean_values_100.get(r):
									mean_values_100[r] = 0.0
								mean_values_100[r] += 1 
								size_n[time_diff] += 1

							if time_diff == 250:
								r = math.sqrt(atom1.distance_sq(atom2))
								if not mean_values_250.get(r):
									mean_values_250[r] = 0.0
								mean_values_250[r] += 1 
								size_n[time_diff] += 1


	od_1 = {key:mean_values_1[key] for key in sorted(mean_values_1.keys())}
	od_30 = {key:mean_values_30[key] for key in sorted(mean_values_30.keys())}
	od_100 = {key:mean_values_100[key] for key in sorted(mean_values_100.keys())}
	od_250 = {key:mean_values_250[key] for key in sorted(mean_values_250.keys())}

	vhove_x_1 = []
	vhove_y_1 = []

	vhove_x_30 = []
	vhove_y_30 = []

	vhove_x_100 = []
	vhove_y_100 = []

	vhove_x_250 = []
	vhove_y_250 = []

	for k in od_1:
		vhove_y_1.append(od_1[k]/size_n[0])
		vhove_x_1.append(k)

	for k in od_30:
		vhove_y_30.append(od_30[k]/size_n[30])
		vhove_x_30.append(k)

	for k in od_100:
		vhove_y_100.append(od_100[k]/size_n[100])
		vhove_x_100.append(k)

	for k in od_250:
		vhove_y_250.append(od_250[k]/size_n[250])
		vhove_x_250.append(k)

	#print(str(key) + ": " + str(round(mean_values_1[key]/size_n[1],2)))

	plt.plot(vhove_x_1, vhove_y_1, color = 'r')
	plt.plot(vhove_x_30, vhove_y_30, color = 'g')
	plt.plot(vhove_x_100, vhove_y_100, color = 'b')
	plt.plot(vhove_x_250, vhove_y_250, color = 'y')

	plt.title("Van Hove correlation")
	plt.legend(["t = 0", "t = 30", "t = 100", "t = 250"])
	plt.show()
