# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 18.6

start, stop = map(int, input().split())
 
i = start
 
while True:
    if i>stop:
        break
    if i%10==3:
        i+=1
        continue
    print(i, end=' ')
    i += 1