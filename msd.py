""" Function to calculate Mean Square Displacement """
import matplotlib.pyplot as plt
import atom
import frame

def plot_MSD(list_frames): 
    """ To calculate Mean Square Displacement """
    mean_values = {}
    size_n = {}
    len_frames = len(list_frames)

    for frame1 in list_frames:
        for frame2 in list_frames:
            if frame2.time <= frame1.time:
                continue
            
            time_diff = frame2.time - frame1.time
            for atom1, atom2 in zip(frame1.atoms, frame2.atoms):
                mean_values[time_diff] = mean_values.get(time_diff, 0) + atom1.distance_sq(atom2)
                size_n[time_diff] = size_n.get(time_diff, 0) + 1

    print(len_frames)
    print(mean_values)
    msd_list = []

    for key in mean_values:
        msd_list.append(mean_values[key]/size_n[key])

    # Diffusion Constant
    #value = (msd_list[::-1] - msd_list[::-50])/(50.0*6)

    #print("Diffusion Constant: " + str(value))

    print(msd_list)
    plt.plot(msd_list, color = 'r')
    plt.show()
