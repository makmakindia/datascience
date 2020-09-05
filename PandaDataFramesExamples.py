# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:41:06 2020

@author: ARUNM

Panda dataframes III

Summary
Import data 
Concise summary of dataframes
converting variables data types using astype
Category Vs Object data type determine size using nbytes
Cleaning column Doors values Cleans 'three' as '3' using  replace 
Getting count of missing values  isnull().sum()

Control structures 
if elif family 
For
While
Functions - single prama, multiple param

"""



import pandas as pd
import numpy as np


cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
print(cars_data)

# print values of initial dtypes
print(" ************************ print values of initial dtypes ****************")
print(cars_data.info())


#Convert variable's data types, astype method is sued to explicitly convert data types
cars_data['MetColor']=cars_data['MetColor'].astype('object')
cars_data['Automatic']=cars_data['Automatic'].astype('object')

           
# print values after converting MetColor and Automatic column data types explicitly.
print("*******************after converting MetColor and Automatic column *************** ")
print(cars_data.info())
"""
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 5   MetColor   1286 non-null   object 
 6   Automatic  1436 non-null   object 
"""

# Category Vs Object variables data types , nbytes() used to get the total bytes consumed by the elements of columns

print("******* Object size ******* ",cars_data['FuelType'].nbytes)
print(" ************ category size *********",cars_data['FuelType'].astype('category').nbytes)

#Before replacing values 
print("************************ Unique values usinf np module ************************")


print(np.unique(cars_data["Doors"]))

print("************************ END Unique values usinf np module ************************")
# replace desired values 
print("****************** started replace desired values ******************")
cars_data['Doors'].replace('three','3',inplace=True)
cars_data['Doors'].replace('four','4',inplace=True)
cars_data['Doors'].replace('five','5',inplace=True)

print(np.unique(cars_data["Doors"]))
print("ENDED replace desired values ")

print(" **********************started Convert data types ***********************")
cars_data['Doors']=cars_data['Doors'].astype('int64')
print(cars_data.info())

# to detect missing values is used isnumm.sum()
print(" **********************started finding NULL value count  ***********************")
print(cars_data.isnull().sum())

# control structures 
cars_data1=cars_data
print(cars_data1)
#adding a colums to sheet

print("************************ adding a colums to sheet *********************************")
cars_data1.insert(10,"Price_Class","")
#print(cars_data1)

print("************** FOR LOOOP")
i=0
for i in range(0,len(cars_data1['Price']),1):
    if(cars_data1['Price'][i]<=8450):
        cars_data1['Price_Class'][i]="Low"
    elif(cars_data1['Price'][i]>13950):
        cars_data1['Price_Class'][i]="High"
    else:
        cars_data1['Price_Class'][i]="Medium"
        

print(cars_data1['Price_Class'].value_counts())


cars_data1.insert(11,"Age_Converted",0)

# function Convert  age from oths to years

# def c_convert(val):
#     val_converted=val/12
#     return val_converted

# cars_data1["Age_Converted"]=c_convert(cars_data1['Age'])
# cars_data1["Age_Converted"]=round(cars_data1["Age_Converted"],1)

#Multiple values functions

cars_data1.insert(12,"km_per_month",0)

print(cars_data1.head())
def c_convert(val1,val2):
    val_converted=val1/12
    ratio=val2/val1
    return [val_converted,ratio]

cars_data1["Age_Converted"],cars_data1["km_per_month"]=  c_convert(round(cars_data1['Age']),round(cars_data1['KM']))
     
print(cars_data1.head())


