# do HOGSVD. All you need to know to use it is:
# data is a list of numpy arrays.
# each numpy array has the same number of columns

import numpy as np

def hogsvd(data):
    '''
    data is a list of numpy arrays. Each has the same number of columns, but a different 
    number of rows.
    ''' 

    # let n be the number of columns each array should have
    _ , n  = data[0].shape
    
    # test to see if the data we get is good
    i = 0
    for d in data:

        # do all matrices have same number of columns 
        errStr =  str(i) + "th dataset has " + str(d.shape[1]) + " columns, not " + str(n) +"." 
        assert d.shape[1] == n , errStr
        
        # do the data matrices have full rank?
        r = np.linalg.matrix_rank(d)
        assert r >= n , "The " + str(i) + "th dataset does not have full column rank"

        # increment counter, so we know which entry we are using
        i = i+1
        

    # number of datasets
    N  = len(data) 

    # create a list of A's and its inverse
    A = []
    Ainv = []
    for d in data:
        a = np.einsum( " ji , jk -> ik " , d,d) # calculate Ai
        A.append( a ) # append it to the list of A's 
        Ainv.append(np.linalg.inv( a ) ) # append inverse to list of inverses





    # calcualte the matrix S - equation (2) in the paper
    S = 0
    for i in range(N):
        for j in range(i+1, N):
                  
            # calculate Sij as in the paper
            Sij = ( np.einsum( "ij , jk ->ik " , A[i] , Ainv[j] )
                    + np.einsum( "ij , jk -> ik" ,  A[j] , Ainv[i] ) 
                    ) /2.0
            assert Sij.shape == (n,n) , "Sij is not n by n"
            S = S + Sij

    # finish with averaging
    S =  2.0*S  /  (N*(N-1))

    # extract eigenvalues, like the end of equation (2) in the paper
    w , V = np.linalg.eig(S)

    # find the U's - corresponds to equations (3) and (4) in the paper
    U = []
    Sigma =[]
    for D in data:
        b = np.linalg.solve(V , np.transpose(D) ) # solve linear system of equations, as in (3)
        b = np.transpose( b ) 
        sigma = np.sqrt ( np.sum( b*b, 0 ) ) # sigma is a vector with entries as in (4)
        u = b/sigma
        Sigma.append( sigma )
        U.append( u )


    # sanity checks:
    assert len(w) == n , "Error. We have too many eigenvalues for S."
    assert np.all( np.where( w >= 1 ) ) , "Eigenvalues of w smaller than 1!"

    return U , Sigma , V , w



# test it!
if (__name__ == '__main__'):
    n = 4
    datasize = 20
    # create fake data
    data =[]
    for i in range(datasize):

        d = np.random.rand( i+n+datasize, n  )
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

        # reconstruct the ith matrix from its components using einsum,
        # a nice (and fast) way to write matrix products.
        reconstructed = np.einsum( 'ij , j , kj -> ik' , U[i] , S[i] , V)

        # make sure it is close to the original one
        assert np.allclose(reconstructed , data[i] ) , "Failed for " + str(i) +"th dataset."

    print "Test complete."
