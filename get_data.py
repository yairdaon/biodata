import numpy as np

# creates fake data!!!!
def get_fake_arrays(nsets):  
    
    # creates FAKE DATA!!!
    # this needs a script to get the real data

    # the number of timesteps - we have 8
    n = 8

    # how many data sets ("experiments") we got
    datasize = nsets
    
    # create fake data
    data =[]
    for i in range(datasize):
        
        # create random data, i+n+datasize is the "number of genes"
        d = np.random.rand( i+n+datasize, n )

        # append to list
        data.append ( d )
           
    # return list with data mtrices
    return data

def get_good_arrays():
    print "Do something here!!!"
