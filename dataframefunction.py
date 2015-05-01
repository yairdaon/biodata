###
## PURPOSE: to generate a data frame to calculate SVD


## 


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore', 'numpy equal will not check object identity in the future') ##A PYTHON BUG


##Primer: for the input of this function, take a Cleaned CSV file (NO NA ROWS), this means that rows with NAs across are gone
## I added the NA exception for protein IDs that are found but not identified by a gene, which I filtered out

##Run Example = DATAFRAMER_Prot('no_NA_proteindata.csv','LFQ.intensity.','LFQ.intensity.1_0h_RS1')
##This runs the Label Free Quantified expression 
def DATAFRAMER_Prot(fil,patt,pat1):
    with open(fil)as f: ##open the file which is a csv
        df1 = pd.read_csv(f,index_col='Gene.names',na_values=['NA']) ##use_gene_ids as rownames
        dd= df1[(df1.Contaminant!='+') &(df1.Reverse!='+')] ##filter out '+' in Reverse/Contaiminant columns
        vv= pd.DataFrame(dd.filter(regex=patt))
        vv= vv[np.isfinite(vv[pat1])]
        #add if clause
        #del vv[pat1]


    #make an array
    data_array = np.asarray(vv)
    
    # get number of columns
    _ , n = data_array.shape
    
    # get the first experiment
    experiment1 = data_array[:,0:2*n:2]

    # get the second experiment
    experiment2 = data_array[:,1:2*n:2]

    # average first ands second experiments
    average = (experiment1 + experiment2)/2.0

    return average

#def DATAFRAMER_Prot(fil,patt,pat1):
   # with open(fil)as f: ##open the file which is a csv
       # df1 = pd.read_csv(f) ##use_gene_ids as rownames / NA exception for missing genes*2
       #dd= df1[(df1.C


##NEXT STEPS##
##1.Normalize Values
##2.Calculate SVD/ (HOGSVD??)
##3. Extract the Genes and the biological relevancy of the Eigen Vectors





