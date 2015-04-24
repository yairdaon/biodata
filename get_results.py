import numpy as np
import matplotlib.pyplot as plt

import get_data
import hogsvd as hog

# set up steps:
nSets    = 3 # assume we have three data sets


# get the data as a list of numpy arrays
data = get_data.get_np_arrays()

# perform hogsvd
U , sigma ,V , commonInd = hog.hogsvd(data)


# time steps we use for experiments
times = np.array([0,0.5, 1 , 2 ,8,  16 ,24 ,30 ] ) 
n = len(times)

# here we create plots for the first higer order eigen genes
for i in commonInd:

    fig = plt.figure()
    for d in data:

        
        # red dashes, blue squares and green triangles
        plt.plot(times, times, 'r--') #, times, times*2, 'bs', times, times*3, 'g^')
        plt.show()
