
import numpy as np
import dataframefunction as dff

# get the data
vv = dff.DATAFRAMER_Prot('no_NA_proteindata.csv',
			'LFQ.intensity.','LFQ.intensity.1_0h_RS1')

#make an array
data = np.asarray(vv)

# get the first experiment
sam1 = data[:,0:-1:2]

# get the second experiment
sam2 = data[:,1:-1:2]

# average first ands second experiments
avg = (sam1+sam2)/2.0

# do SVD on de averaged data
U , S, V = np.linalg.svd(avg)


