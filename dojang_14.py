# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 14.7

korean, english, math, science=map(int,input().split())
x=(korean+english+math+science)/4
 
if korean<0 or korean>100 or english<0 or english>100 or math<0 or math>100 or science<0 or science>100:
    print('잘못된 점수')
 
else:
    if x>=80:
        print('합격')
    else:
        print('불합격')
