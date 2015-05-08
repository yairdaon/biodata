import numpy as np
import dataframefunction as dff
import readdata as rd
import NewRNA as nu
import pandas as pd

def subtract_row_mean(arr):  
    # Calculate the mean of every row - this means sum over column index. Therefore, axis=1
    rowMean = np.mean(arr,axis= 1)

    # subtract the mean
    arr     = arr - rowMean[:,np.newaxis]
    
    return arr

def divide_by_std(arr):

    # calculate row standard deviation
    sigma  = arr.std(axis=1)

    # divide each row by its standard deviation
    arr    = arr / sigma[:,np.newaxis]

    return arr
 
def divide_by_row_mean(arr):
    # Calculate the mean of every row - this means sum over column index. Therefore, axis=1
    rowMean = np.mean(arr,axis= 1)

    # divide each row by its standard deviation
    arr    = arr / rowMean[:,np.newaxis]

    return arr
   

def divide_by_row_max(arr):
    # Calculate the max of every row
    rowMax = arr.max(axis= 1)

    # divide each row by its standard deviation
    arr    = arr / rowMax[:,np.newaxis]

    return arr
# creates fake data!!!!
def get_fake_arrays(nsets, n=8):  
    
    # creates FAKE DATA!!!
    # this needs a script to get the real data
    # n is the number of columns (times steps) - we have 8
    
    
    # create fake data
    data =[]
    for i in range(nsets):
        
        # create random data, i+n+datasize is the "number of genes"
        d = np.random.rand( (i+1)*n*nsets*100, n )

        # process it somehow
        d = divide_by_row_mean( d )

        # append to list
        data.append ( d )
           
    # return list with data mtrices
    print data[0].shape
    print data[1].shape
    return data


# get actual (real, experimental!!!) data
def get_good_arrays():
   
    # an empty list of numpy arrays
    data_list = []
     
    # an empty list for names
    name_list = []

    # get protein data and protein names
    prot ,prot_names = dff.DATAFRAMER_Prot('no_NA_proteindata.csv',
			'LFQ.intensity.','LFQ.intensity.1_0h_RS1')

    # get RNA data and names
    rna ,rna_names = nu.read_RNA('RNA_normalized_filtered_LOWESSsmoothed.txt')
    
    # normalize 
    prot = divide_by_row_max( prot )
    rna  = divide_by_row_max( rna  )
    
    data_list.append(prot)
    data_list.append(rna)

    name_list.append(prot_names)
    name_list.append(rna_names )

    return data_list , name_list
