#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 01:59:53 2020

@author: kaarthika
"""

x=10
def func(num):
    x=5
    for i in num:
        x*=i
        print(x)
    return x

print(func((-2,-1,1,2,3)))    