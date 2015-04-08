# a function that performs Higher Order SVD, as suggested in Ponapalli et al.

import numpy as np

def hogsvd(data):
    '''
    data is a list of numpy arrays. Each has the same number of columns, but a different 
    number of rows.
    
    '''

    # ideally we would have some tests here to check whether the data is good:
    # do the data matrices have full rank?
    # do all matrices have same number of columns 

    _ , n  = data[0].shape
    N  = len(data) # number of datasets we have

    A = []
    Ainv = []
    # create a list of A's and its inverse
    for D in data:
        a = np.dot( np.transpose(D) , D) # calculate the current A  
        A.append( a ) # append it to the list of A's 
        Ainv.append(np.linalg.inv( a ) ) # append its inverse to the list of inverses


    # calcualte the matrix S - equation (2) in the paper
    S = 0
    for i in range(N):
        for j in range(i+1, N):
                                         
            Sij = ( np.dot( A[i] , Ainv[j] ) + np.dot( A[j] , Ainv[i] ) ) /2.0
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
n = 2
# create fake data
data =[]
for i in range(6):
    d = np.random.rand(i+n+1, n)
    data.append ( d )


U , S , V = hogsvd(data)

# make sure dimensions are what we expect
for i in range(len(data)):
    assert U[i].shape[0] == n+i+1 , str(U[0].shape[0])+ " !=  " + str( n ) 
    assert U[i].shape[1] == n
    assert len(S[i])  == n
    assert V.shape[0] == V.shape[1]
    assert V.shape[0] == n


    reconstructed = np.einsum( 'ij , j , kj -> ik' , U[i] , S[i] , V)
    diff = reconstructed - data[i]
    diff = diff*diff
    print(str(i) + "th iteration, residual = " +str(np.sum(diff)))
