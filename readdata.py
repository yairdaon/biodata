import csv
import optparse


def readcsv(filename):
   """
   read the csv file to get the information of patients
   """
   f=open(filename,"r")
   readers=csv.DictReader(f)
   headers=readers.fieldnames
   return headers,readers

if __name__=="__main__":
   parser=optparse.OptionParser()
   
   parser.add_option("-C", dest="CSVfile",default="",help="full pathname of CSV file")
   
   #load the inputs
   (options,args)=parser.parse_args()   
   CSVfile=options.CSVfile
   
   headers,readers=readcsv(CSVfile)
   