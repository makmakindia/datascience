#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:34:35 2020

@author: kaarthika

github repository URL
https://github.com/makmakindia/datascience.git


email : makmakindia@gmail.com

1) How to import  OS & panda libaraies 
2) Howc to gehan working directory using OS library 
3) How ot work with csv files 
4) this lecture is all about how to read different data fiels formats into spyder using pandas.



"""

import os 
import pandas as pd


os.chdir("/home/kaarthika/spyderdemo/datascience")
# read cs vdata file
#data_csv=pd.read_csv("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.csv")
# how t oremove unwanted columns in file index_col=0
data_csv=pd.read_csv("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.csv",index_col=0)

# replace all missing  / junk values in spyder as NaN, replace all junk missing values as NaN using na_values=["??"]
data_csv=pd.read_csv("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.csv",index_col=0,na_values=["??"])

# how to read xlsx format file 
data_xlsx=pd.read_excel('/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.xlsx',sheet_name='Iris_data',index_col=0,na_values=["###"])


#how t oread flat files data 
data_txt1=pd.read_table("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.txt",index_col=0, na_values=["??"])

#how to seprate data with \t is Sep='\t' or deleimiter='\t' or delimiter = " "
#data_txt1=pd.read_table("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.txt",sep='\t', na_values=["??"])
data_txt1=pd.read_table("/home/kaarthika/spyderdemo/datascience/datasets/Iris_data_sample.txt",delimiter=" ", index_col=0,na_values=["??"])