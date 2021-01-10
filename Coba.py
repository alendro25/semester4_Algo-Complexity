# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:33:50 2020

@author: G-470
"""

def fungsi(n):
	if n < 0 :
    	 print("tidak ada bilangan negatif")
        
	if n == 0 or n == 1 : 
            return n;
    
	else :
			return fungsi(n-1) + fungsi(n-2)


hasil = fungsi(5)
print "  Deret Fibonacci ke-? adalah = (%d) " % (hasil)