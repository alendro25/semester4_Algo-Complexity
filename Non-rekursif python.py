# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:11:36 2020

@author: G-470
"""

a, b, c = 0,1,0
for i in range(20):
    print a,
    c=a+b
    a=b
    b=c
    