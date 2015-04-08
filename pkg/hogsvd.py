# do HOGSVD. All you need to know to use it is:
# data is a list of numpy arrays.
# each numpy array has the same number of columns

import numpy as np

def hogsvd(data):
    '''
    data is a list of numpy arrays. Each has the same number of columns, but a different 
    number of rows.
    
    ''' 

    # initialize n to be the umber of columns each array should have
    _ , n  = data[0].shape
    i = 0

    # test to see if the data we get is good
    for d in data:

        # do all matrices have same number of columns 
        assert d.shape[1] == n , "The " +str(i) + "th dataset has " + str(d.shape[1]) + " columns. It should have " + str(n) + "." 
        
        # do the data matrices have full rank?
        r = np.linalg.matrix_rank(d)
        assert r >= n , "The " + str(i) + "th dataset does not have full column rank"

        # increment our counter, so we know which entry we are using
        i = i+1
        
    # number of datasets we have
    N  = len(data) 


    # create a list of A's and its inverse
    A = []
    Ainv = []
    for d in data:
        a = np.einsum( " ji , jk -> ik " , d,d) 
        #a = np.dot( np.transpose(D) , D) # calculate the current A  
        A.append( a ) # append it to the list of A's 
        Ainv.append(np.linalg.inv( a ) ) # append its inverse to the list of inverses





    # calcualte the matrix S - equation (2) in the paper
    S = 0
    for i in range(N):
        for j in range(i+1, N):
                                         
            Sij = ( np.einsum( "ij , jk ->ik " , A[i] , Ainv[j] ) + np.einsum( "ij , jk -> ik" ,  A[j] , Ainv[i] ) ) /2.0
            S = S + Sij

    # finish with averaging
    S =  S  /  (N*(N-1))

    # extract eigenvalues, like the end of equation (2) in the paper
    w , V = np.linalg.eig(S)

    # find the U's - corresponds to equations (3) and (4) in the paper
    U = []
    Sigma =[]
    for D in data:
        b = np.linalg.solve(V , np.transpose(D) ) # solve the linear system of equations, this is (3)
        b = np.transpose( b ) 
        sigma = np.sqrt ( np.sum( b*b, 0 ) ) # sigma is represented as a vector with entries like in (4)
        u = b/sigma
        Sigma.append( sigma )
        U.append( u )

    return U , Sigma , V



# test it!
n = 4
datasize = 20
# create fake data
data =[]
for i in range(datasize):
    d = np.random.rand(i+n+datasize, n)
    data.append ( d )

# get the hogsvd 
U , S , V = hogsvd(data)

for i in range(len(data)):

    # check that all the dimensions match
    assert U[i].shape[0] == n+i+datasize 
    assert U[i].shape[1] == n
    assert len(S[i])  == n
    assert V.shape[0] == V.shape[1]
    assert V.shape[0] == n

    # reconstruct the ith matrix from its components (einsum is a nice and fast way to write matrix products. I can explain it!)
    reconstructed = np.einsum( 'ij , j , kj -> ik' , U[i] , S[i] , V)

    # make sure it is close to the original one
    assert np.allclose(reconstructed , data[i] ) 
