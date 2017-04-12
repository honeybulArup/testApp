import numpy as np 
import pandas as pd 
import urllib
import os 

''' 
Useful Information;

Year; 'Year'
Road Name; ''Common_Road_Name'
Severity; 'Severity' [nan, Hospital, Property Damage Only (Major), Property Damage Only (Minor)
            Fatal, Medical]
Accident Type; 'Acc_Type' [Intersection, Midblock]
Total_Truck
Total_Motor_Cycle
Total_Pedestrian
Total_Bike
Total_Others_Vehicles
Total_Heavy_Truck 
Total_Animal
'''

def read_data(colnames):
    os.chdir('C:\\Users\\Robert.Honeybul\\Desktop\\testApp\\python')
    df = pd.read_csv('data/data.csv')
    df = df[colnames]
    df = df.fillna(0)
    return df

def main():
    colnames = ['Lat',
                'Long',
                'Year', 
                'Common_Road_Name', 
                'Severity', 
                'Acc_Type', 
                'Total_Truck', 
                'Total_Motor_Cycle', 
                'Total_Pedestrian', 
                'Total_Bike', 
                'Total_Others_Vehicles', 
                'Total_Heavy_Truck']         

    data = read_data(colnames)
    
    for i in xrange(len(data.index)):
        
    
    print len(data.index)

if __name__ == '__main__':
    main()


"""

client = MongoClient('mongodb://honeybulr:Fender10@ds159279-a0.mlab.com:59279,ds159279-a1.mlab.com:59279/cultured-cities?replicaSet=rs-ds159279')
db = client['cultured-cities']

print '\n'

print 'Seeding Database ...'
collection_name = 'PerthBuilding' 
db[collection_name].drop()

db[collection_name].insert_many([dev_dict[i] for i in range(len(dev_dict))])
    
db[re.sub("Building","",collection_name)].drop()
db[collection_name].rename(re.sub("Building","",collection_name))

print 'Finished seeding Database ... '

print '\n'

"""
