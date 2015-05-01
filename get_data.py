import numpy as np
import dataframefunction as dff
import readdata as rd

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
   

    data =[]
    rna = rd.readcsv('RNA_normalized_filtered_LOWESSsmoothed.txt')
    data.append(rna)
    
    

    # get the data
    vv = dff.DATAFRAMER_Prot('no_NA_proteindata.csv',
			'LFQ.intensity.','LFQ.intensity.1_0h_RS1')
    
    #make an array
    data = np.asarray(vv)
    n= len(data[0,:])/2
    

    # get the first experiment
    sam1 = data[:,0:2*n:2]

    # get the second experiment
    sam2 = data[:,1:2*n:2]

    # average first ands second experiments
    avg = (sam1+sam2)/2.0

    print rna.shape
    print avg.shape
    data.append(avg)
