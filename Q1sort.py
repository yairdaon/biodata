
import dataframefunction;
import numpy;
import pandas;

vv=dataframefunction.DATAFRAMER_Prot("no_NA_proteindata.csv",'LFQ.intensity.','LFQ.intensity.1_0h_RS1')

names=vv.index
data=vv.values
firstp=data[:,0:len(data[0,:]):2]
secondp=data[:,1:len(data[0,:]):2]
avg=(firstp+secondp)/2
U , S, V = numpy.linalg.svd(avg)

for i in range(len(names)):
    print (names[i])
        
for i in range(0,8):
    temp=U[:,i]
    pdtemp=pandas.Series(temp,names);
    pdtemp.sort();
    stname=""
    val=""
    for i in range(len(pdtemp.index)):
        if (pdtemp.index[i]==nan):
                    print ("yes")        
        stname=stname+str(pdtemp.index[i])+"\t"
        val=val+str(pdtemp[i])+"\t"
    print (stname)
    print (val)
        


