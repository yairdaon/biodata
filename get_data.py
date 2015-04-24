import numpy as np

def get_np_arrays():  
    
    # creates FAKE DATA!!!
    # this needs a script to get the real data

    # the number of timesteps - we have 8:  0,15,30,60,90,120 (???)
    n = 8

    # assume we have three data sets
    datasize = 3
    
    # create fake data
    data =[]
    for i in range(datasize):
        
        # create random data, i+n+datasize is the "number of genes"
        d = np.random.rand( i+n+datasize, n )

        # append to list
        data.append ( d )
           
    # return list with data mtrices
    return data
