import csv
import numpy as np
import pandas as pd
import optparse

def read_RNA(fil):
   df = pd.read_csv(fil , sep=None)

   # get data as stupidly as possible
   t0  = df.R1t0  + df.R3t0
   t05 = df.R1t05 + df.R3t05
   t1  = df.R1t1  + df.R3t1
   t2  = df.R1t2  + df.R3t2
   t8  = df.R1t8  + df.R3t8  
   t16 = df.R1t16 + df.R3t16  
   t24 = df.R1t24 + df.R3t24
   t30 = df.R1t30 + df.R3t30

   readers = [t0, t05 ,t1 ,t2 ,t8 ,t16 ,t24 ,t30]
   readers = np.array(readers) 
   readers = np.transpose( readers/2.0 )
 
   rnas , times = readers.shape
   print rnas ,times
   assert times == 8, BAAAD

   st = times/2
   rna1  = readers[:,0:st]
   rna3  = readers[:,st:times-1]
   
   rna = (rna1 +  rna3)/2.0

   # do the data matrices have full rank?
   r = np.linalg.matrix_rank(rna)
      
   if ( r < times/2):
      print "rank = " +str(r)
      print "number of columns = " +str(times/2)
      
   return rna

def call():
   return read_RNA('RNA_normalized_filtered_LOWESSsmoothed.txt')

if __name__=="__main__":
   read_RNA('RNA_normalized_filtered_LOWESSsmoothed.txt')
   
