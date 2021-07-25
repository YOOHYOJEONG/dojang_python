# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 24.5

a = input().split()

count = 0 
for i in a :
    if i.strip(',.') == 'the' :
        count += 1

print(count)