import numpy as np
import dataframefunction as dff
import readdata as rd
import pandas as pd

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


# get actual (real, experimental!!!) data
def get_good_arrays():
   
    # an empty list of numpy arrays
    data_list=[]
     
    # get protein data
    prot = dff.DATAFRAMER_Prot('no_NA_proteindata.csv',
			'LFQ.intensity.','LFQ.intensity.1_0h_RS1')

    # get RNA data
    rna = rd.read_RNA('RNA_normalized_filtered_LOWESSsmoothed.txt')

    data_list.append(prot)
    data_list.append(rna)

    return data_list
