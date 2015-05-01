import numpy as np
import matplotlib.pyplot as plt

import get_data
import hogsvd as hog
import dataframefunction as dff

# for reproducibility, set the random number generator's seed
np.random.seed(17) # 17 is the most random number of all!!

# plot stuff, not interesting
colors = [ 'r' , 'b' , 'g' ,'c', 'm', 'y', 'k']

# get the data as a list of numpy arrays
#data = get_data.get_fake_arrays(3) # now we use FAKE data
data  = get_data.get_good_arrays()
nSets = len(data) # number of data sets

# perform hogsvd
U , sigma ,V , w = hog.hogsvd(data)

# get indices of eigenvalues with equal significance
goodIndices = np.ravel( np.where( w < 1.5 ) )

# time steps we use for experiments
times = np.array([0,0.5, 1 , 2 ,8,  16 ,24 ,30 ] ) 


# here we gather expression levels of  the first higer order eigen genes
# across time, in each dataset:
#=======================================================================

# this list will hold the expression levels
# loop over all equal significance indices
for i in goodIndices:
    curves =[] 

    # loop over all data sets
    for j in range(nSets):

        d = data[j] # d is now the jth data set
        u = U[j]    # u is now the jth matrix of eigengenes
    
        # sanity checks
        assert u.shape[0] == d.shape[0]
        assert u.shape[1] == d.shape[1]

   
        eigenGene = u[:,i] 
        if(  d.shape[0] != len(eigenGene) ):
            raise ValueError('dimension mismatch in data matrix and eigengene.')
        
        # the expression pattern of ith eigengene in jth dataset
        expression = np.einsum( 'ij, i -> j' , d, eigenGene)
        
 
        curve =  plt.plot(times, expression, 
                          label = str(i)+ "th eigengene in "+ str(j) + "th experiment." )
        plt.setp( curve, 'linewidth', 3.0, 'color', colors[j] , 'alpha', .5 )

    plt.legend(loc = 1 , prop ={'size':7})
    plt.title("expression of " + str(i) + "th eigengen across experiments")
    plt.savefig("Expression of " + str(i) + "th eigengene")
    plt.close()

