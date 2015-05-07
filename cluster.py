import pandas as pd
import numpy as np
import csv

def read_file(fil):
    # load data into pndas dataframe
    df = pd.read_csv(fil , sep=None)  
    
if __name__=="__main__":
    read_file("clean.txt")