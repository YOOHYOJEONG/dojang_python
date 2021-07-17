# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 21.6


import turtle as t
 
n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)