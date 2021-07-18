# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 22.10

a,b = map(int, input().split())
List = [2 ** i for i in range(a,b + 1)]
del List[1]
del List[-2]
print(List)