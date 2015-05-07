import csv
import numpy as np
import pandas as pd

def read_RNA(fil):

   # load data into pndas dataframe
   df = pd.read_csv(fil , sep=None)

   # get rna names
   names = df.index
   
   # get data as stupidly as possible
   t0  = df.R1t0  + df.R3t0   # t == 0  hours 
   t05 = df.R1t05 + df.R3t05  # t == 0.5 hours
   t1  = df.R1t1  + df.R3t1   # t == 1 hour
   t2  = df.R1t2  + df.R3t2   # etc.
   t8  = df.R1t8  + df.R3t8  
   t16 = df.R1t16 + df.R3t16  
   t24 = df.R1t24 + df.R3t24
   t30 = df.R1t30 + df.R3t30


   # put them all in a list
   rna = [t0, t05 ,t1 ,t2 ,t8 ,t16 ,t24 ,t30]
   
   # make it an array and average
   rna = np.array(rna)/2.0

   # transpose so times are columns
   rna = np.transpose( rna )
       
   return rna ,names

if __name__=="__main__":
   read_RNA('RNA_normalized_filtered_LOWESSsmoothed.txt')
   
