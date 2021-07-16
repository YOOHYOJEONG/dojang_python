# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 19.6

a  = int(input())
for i in range(a) :
    for j in reversed(range(a)) :
        if i < j :
            print(' ', end = '')
        else :
            print("*", end = '')
    for j in range(a):
        if i>j :
            print('*', end='')
            
    print()