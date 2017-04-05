import numpy as np 
import pandas as pd 
from init import read_data 

def main():
    data = read_data()
    
    print data.head()

if __name__ == '__main__':
    main()