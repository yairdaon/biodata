
# get the data
vv = DATAFRAMEFUNCTION(... . ...)

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




###
most_sig_eig_gene = U[:,0]

most_sig_eig_gene
Out[42]:
array([-0.00021219, -0.00034019, -0.0005811 , ..., -0.00074133,
       -0.00041571, -0.0005057 ])
