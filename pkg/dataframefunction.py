###Readin dataframewith csv, takes as input the filename and the pattern of the interested columns
## you guys can alter it to be indices

import pandas as pd

def DATAFRAMER_Prot(fil,patt):
    with open(fil)as f: ##open the file which is a csv
        df1 = pd.read_csv(f,index_col='Gene.names') ##use_gene_ids as rownames
        dd= df1[(df1.Contaminant!='+') &(df1.Reverse!='+')] ##filter out '+' in Reverse/Contaiminant columns  
        vv= pd.DataFrame(dd.filter(regex=patt)) ## used a flexible rgx expression to get the columns we would want..I'll explain later
    return vv

file = 'no_NA_proteindata.csv' ##pre-filtered data_file using R, emailed last week
patt = 'Razor...unique.peptides' ## number of unique proteins with control..can explain later
DATAFRAMER_Prot(file , patt )



##PROBLEM = 1st column is WRONG, doesn't have a timepoint..someone can come up with a clever REGEX!!

###in this case, we will get back 17 columns(1st is not needed), sample 1 = RS1 / Sample 2 = RS3 ( @ 8TP..should have 16 but note error) ##
## RS = ribosomal stress induced by tunicamycin, I don’t see any controls(untreated) on this haha, i’ll have to double check..
## we would need a different function to remove NAs / deal with NAs if using Python

## 
