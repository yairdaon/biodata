import numpy as np
import matplotlib.pyplot as plt

import get_data
import hogsvd as hog

# for reproducibility, set the random number generator's seed
np.random.seed(17) # 17 is the most random number of all!!

# plot stuff, not interesting
plotOptions = [ 'r--' , 'bs' , 'g^']

# set up steps:
nSets    = 3 # assume we have three data sets

# get the data as a list of numpy arrays
data = get_data.get_fake_arrays(nsets) # now we use FAKE data
n = len(data)

# perform hogsvd
U , sigma ,V , w = hog.hogsvd(data)

# get indices of eigenvalues with equal significance
goodIndices = np.ravel( np.where( w < 1.5 ) )
print w
print goodIndices

# time steps we use for experiments
times = np.array([0,0.5, 1 , 2 ,8,  16 ,24 ,30 ] ) 
n = len(times)

# here we create plots for the first higer order eigen genes

# loop over all data sets
for j in range(n):
    
    d = data[j] # d is the jth data set
    u = U[j]  # u is the jth matrix of eigengenes
   
    # sanity checks
    assert u.shape[0] == d.shape[0]
    assert u.shape[1] == d.shape[1]

    # loop over all equal significance indices
    for i in goodIndices:
        eigenGene = u[:,i] 
        if(  d.shape[0] != len(eigenGene) ):
            raise ValueError('dimension mismatch in data matrix and eigengene.')
        expression = np.einsum( 'ij, i -> j' , d, eigenGene)
 
        # red dashes, blue squares and green triangles
        plt.plot(times, expression, plotOptions[j] )
        plt.title("Expression of " + str(i) + "th eigengene in "+ str(j) + " dataset (experiment).")
        plt.show()
