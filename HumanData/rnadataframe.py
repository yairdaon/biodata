import numpy as np
import pandas as pd

vv = pd.read_csv('RNA_normalized_filtered_LOWESSsmoothed.txt', sep=None)

t0 = (vv.R1t0 + vv.R3t0)/2.0
#t05 = (vv.R1t0.5 + vv.R3t0.5)/2.0
t1 = (vv.R1t1 + vv.R3t1)/2.0
t2 = (vv.R1t2 + vv.R3t2)/2.0
t8 = (vv.R1t8 + vv.R3t8)/2.0
t16 = (vv.R1t16 + vv.R3t16)/2.0
t24 = (vv.R1t24 + vv.R3t24)/2.0
t30 = (vv.R1t30 + vv.R3t30)/2.0

RNA2=pd.read_table('HeLa_RNA_normalized_filtered.txt',index_col=0)

return RNA2
