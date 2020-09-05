# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 06:16:37 2020

@author: ARUNM
"""

# Part - 1
# how to chnage the working directory
# You can try CD <folder path > at console
import os
os.chdir("D:\\Python\\NPTEL_ANCONDA\\PythonDataScience\\spyder_workdir")


#Variables 
a=10
b=a*10
print(a,b)


# Part - 2 
#How to execute python file ?  F9 , Ctrl + Enter , Green RUN button
# How to execute piece of code ?
# How to add comments ? ctrl+1
# how to reset and clear console ? ctrl+L or clear commond at prompt, %reset

dia=5
len=4
vol=(dia**2)*len/4

#  del env variables single / multiple 
del a,b, dia

#Basic libraries in pytho 
#NumPy  - Numerical python
# Pandas - Dataframe python
# Matplotlib - Visualization 
# Sklearn - MAchine Learning
# =============================================================================
# import Numpy 
# content = dir(NumPy)
# print(content)
# =============================================================================

# find data type of variables 

Emp_Name="Arun Kumar"
print("Emp_Name data type is " ,type( Emp_Name))
age =45 
print("Age data type is : ",type(age))
hht=175.03
print("data type of hht is ",type(hht))
#  coercing data types ( Covert) datatype(object)

hht=int(hht)
print("hht data type after coerce is " , type(hht))

# =============================================================================
# precedence of operator 
# parenthesis ()
# Exponent **
# Division /
# Multiplication * 
# Add /Sub - + , -
# Bitwise AND &
# =============================================================================



