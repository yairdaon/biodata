import csv
import numpy
import pandas
import optparse


def readcsv(filename):
   """
   read the csv file to get the information of patients
   """
   with open(filename,'r') as dest_f:
       data_iter = csv.reader(dest_f, 
                              delimiter ="\t", 
                              quotechar = '"')
       data = [data for data in data_iter]  
   readers = numpy.asarray(data)  
   return readers

if __name__=="__main__":
   parser=optparse.OptionParser()
   
   parser.add_option("-C", dest="CSVfile",default="",help="full pathname of CSV file")
   
   #load the inputs
   (options,args)=parser.parse_args()   
   CSVfile=options.CSVfile
   
   readers=readcsv(CSVfile)
   print (1)
   