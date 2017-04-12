import numpy as np 
import pandas as pd
import os 

os.chdir('C:/Users/Robert.Honeybul/Desktop/testApp') 

def read_data():

    df = pd.read_csv('data/data.csv')
    intx = df['Intx']
    print intx
    return df