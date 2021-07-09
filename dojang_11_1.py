# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 11.8

x = input().split()

del x[-5:len(x)]
print(tuple(x))