
import numpy as np
import dataframefunction as dff
import matplotlib.pyplot as plt


# get the data
vv = dff.DATAFRAMER_Prot('no_NA_proteindata.csv',
			'LFQ.intensity.','LFQ.intensity.1_0h_RS1')

#make an array
data = np.asarray(vv)
n= len(data[0,:])/2
print n

# get the first experiment
sam1 = data[:,0:2*n:2]

# get the second experiment
sam2 = data[:,1:2*n:2]

# average first ands second experiments
avg = (sam1+sam2)/2.0
print avg.shape
# do SVD on de averaged data
U , S, V = np.linalg.svd(avg)

u = U[:,0]

vals = []
for i in range(n):
    d = avg[:,i]
    expr_level = np.dot(d, u)
    vals.append(expr_level)


times = [0, .5,1,2,8,16,24,30]


