# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 15.4

age = int(input())
balance = 9000 

if 7<=age<=12:
    balance-=650
elif 13<=age<=18:
    balance-=1050
elif age>=19:
    balance-=1250
    
print(balance)