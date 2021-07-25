# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 24.6


prices=list(map(int,input().split(';')))
prices.sort(reverse=True)
for i in prices:
    print('{0:>9,}'.format(i))