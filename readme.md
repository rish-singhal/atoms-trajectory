# PSCM - Final Project

[Web Version](https://rish-singhal.github.io/atoms-trajectory/)

### Technologies Used

**Language:** Python          

**Modules:** numpy, matplotlib, pickle, copy, tqdm

### Description

Following steps are implemented:

1. Intially 108 Argon atoms are generated randomly such that length of the box is 18 Angstrom
2. Potential Energy is minimized using gradient descent.
3. Initial velocities are sampled using Maxwell-Boltzman distribution with T = 300 Kelvin
4. Trajectory is generated for ITERATIONS = 300
5. Following plots are plotted:
	- Mean Square Displacement Plot
	- Van Hove Correlation 
	- Velocity Correlation
	- Dynamic Structure Factor
	- Distance Frequency Graph

### Features

1. Command Line Interface
2. The frames once generated for X number of iterations is saved as a file "frames_{ITERATIONS}.pkl"
3. Van hove correlation matrix can also be saved as a file "vanhove_{ITERATIONS}.pkl"

### Instructions 

Instructions to execute the program:

```bash
> python3 main.py
```

After this a command line interface will be available, showing this

```bash
>> help
```
Execute "help" function for the functions which can be called in the program.

### HELP

The following functions are available for command line interface.

```bash

ls ---->                |Print the pkl file names in the current directory
gen ITERATIONS ---->    |Generate ITERATIONS and save in file
load INPUT_FILE ---->   |Provide Input File
load vanhove INPUT_FILE |Provide Input File
plot msd ---->          |Plot Mean Square Displacement
plot vanhove ---->      |Plot Van Hove Correlation
plot vel --->           |Plot Velocity Correlation
plot df --->            |Plot Dynamic Factor
exit ---->              |EXIT
```



### Constants

```python
N = 108 # Number of atoms
LEN = 18e-10 # Angstrom
EPSILON = 1.66e-21 # 0.238 kcal/mol
SIGMA = 3.4e-10 # Angstrom
MIN_DIST = 3.4e-10 # Angstrom

# For gradient descent
DELTA = 0.01 # energy difference to break gradient descent
ETA = 0.1 # learning rate

# For trajectory generation
ITERATIONS = 300 # can be taken as an input too
TIME_STEP = 4e-15 # 4 femto seconds
MASS = 6.633359936e-26 # mass of Argon (in Kg)

#For Sampeling velocities
K = 1.38e-10 # Boltzman Constant
TEMP = 300 # Temperature = 300 Kelvin
```

### Sample Plots for 300 ITERATIONS & Inferences

#### Pair Distance Bar Graph

![](Plots/rij_300.png)

As the minimum distance was given to be 3.4 Angstrom, hence it can be seen in the graph that there is no pair of atoms with distance less than 3.4 Angstrom.

For this graph, the distances were rounded off to the nearest integer. Also, it can be seen that the curve is somewhat follows \~gaussian distribution. This can be due to the random sampling for 108 atoms, and central limit theorem.

#### Mean Square Displacement

![](Plots/msd_300.png)

It can be seen that, MSD value increases as time-difference gap increases intially as a quadratic relation. And then it seems to drop a bit which can be due to application of periodic-boundary conditions. As 1st kind of periodic boundary conditions is used, i.e. if the atom moves left to the box, another atom comes from the right.

#### Van Hove Correlation

![](Plots/vanhove_300.png)

This can be seen to be in line with the Van Hove Correlation function graphs available online, and it follows some kind of \~maxwell distribution i.e. increases first and then after reaching a peak decreases.

For all time-gaps, the graphs seems to be following similar pattern.

#### Velocity Correlation

![](Plots/vel_300.png)

It can be seen that initially the value is the highest and then it drops and becomes flat as time-gap increases. This is because initially when the time difference is less, the vectors for all atoms are somewhat aligned (due to less random nature \~ coming from small time difference) and hence the dot product which is proportional to cos(theta) takes the maxmium value. 

While as time-gap increases, the velocity vectors become highly disaligned compared to the initial position leading to flattening of the curve (due to random nature), and hence showing near to 0 correlation.

#### Dynamic Structure Factor

![](Plots/df_300.png)

The **intermediate scattering** function is the spatial Fourier transform of the van Hove function (which was calculated above), while the **dynamic structure factor** is basically temporal Fourier transform of intermediate scattering funtion.

And in the graph it can be seen that there is a spike initially around k near to 0.


### Deadline

**Phase-1**: 20th April 2021        
**Final**  : 25th April 2021

### Author

**Name:** [Rishabh Singhal](https://rish-singhal.github.io)             
**Roll Number:** 20171213             
**Course Name:** Physics of Soft Condensed Matter, IIIT Hyderabad


