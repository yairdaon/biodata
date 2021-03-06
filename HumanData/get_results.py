import numpy as np
import matplotlib.pyplot as plt

import get_data
import hogsvd as hog
import dataframefunction as dff
import pickle


# for reproducibility, set the random number generator's seed
np.random.seed(17) # 17 is the most random number of all!!

# plot stuff, not interesting
colors = [ 'r' , 'b' , 'g' ,'c', 'm', 'y', 'k']

# experiment names
xp     = ['protein data' , 'RNA data']

# get the data as a list of numpy arrays
#data = get_data.get_fake_arrays(2) # use FAKE data

# data is a list of numpy arrays. names is a list of protein names
# and RNA names (by the same order of experiments)
data , names  = get_data.get_good_arrays()  # use REAL data
nSets = len(data) # number of data sets == number of experiments

# perform hogsvd
U , sigma ,V , w = hog.hogsvd(data)

# get indices of eigenvalues with equal significance
goodIndices = np.ravel( np.where( w < 2.0 ) )
print w

# time steps we use for experiments
times = np.array([0 ,0.5, 1, 2, 8,16 ,24 ,30 ] ) 


# here we gather expression levels of  the first higer order eigen genes
# across time, in each dataset:
#=======================================================================

# this list will hold the expression levels
# loop over all equal significance indices
for i in goodIndices:
    curves =[] 

    list_of_dictionaries = []
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
        
        
        # put eigengene data inside a dictionary
        expression_of_genes_inside_eigengene_with_names = dict(zip(names[j], eigenGene))

        # add to the list of dictionaries that we will soon save
        list_of_dictionaries.append( expression_of_genes_inside_eigengene_with_names )
       


        # the expression pattern of ith eigengene in jth dataset
        expression = np.einsum( 'ij, i -> j' , d, eigenGene)
        
 
        curve =  plt.plot(times, expression, 
                          label = str(i)+ "th eigengene in "+ xp[j] )
        plt.setp( curve, 'linewidth', 3.0, 'color', colors[j] , 'alpha', .5 )


    # do the actual plotting
    plt.legend(loc = 1 , prop ={'size':7})
    tit_str  = "Expression of "+str(i)+"th eigengen. Eigenvalue = " + str(w[i])
    plt.title(tit_str)
    plt.savefig("Expression of " + str(i) + "th eigengene")
    plt.close()

    # save data in pickle
    save_str = "eigen" +str(i)
    output = open(save_str, 'ab+')
    pickle.dump(list_of_dictionaries, output)
    output.close()

    

# This is how one reads "pickle" data:
#output = open('output.txt', 'rb')
#obj_dict = pickle.load(output)    # 'obj_dict' is a dict object


