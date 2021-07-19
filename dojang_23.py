# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:44:43 2021

@author: user
"""

#python dojang uint 23.7

row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
print()


row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
print()
for i in range(row):
    for j in range(col):
        cnt = 0
        if matrix[i][j] == ".":
            if i != 0 and j != 0: 
                if matrix[i-1][j-1] == "*": cnt += 1
            if i != row-1 and j != col-1:
                if matrix[i+1][j+1] == "*": cnt += 1
            if i != 0:
                if matrix[i-1][j] == "*": cnt += 1
            if i != 0 and j != col-1:
                if matrix[i-1][j+1] == "*": cnt += 1
            if j != 0:
                if matrix[i][j-1] == "*": cnt += 1
            if i != row - 1 and j != 0:
                if matrix[i+1][j-1] == "*": cnt += 1
            if j != col -1:
                if matrix[i][j+1] == "*": cnt += 1
            if i != row -1:
                if matrix[i+1][j] =="*": cnt += 1
            matrix[i][j] = cnt
            print(matrix[i][j], end="")
        else:
            print(matrix[i][j], end="")
    print()
    
 
#%%

#simple version

row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
print()
    
for i in range(row):
    for j in range(col):
        cnt = 0
        if matrix[i][j] == ".":
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    if not (y < 0 or x < 0 or y >= row or x >= col):
                        if matrix[y][x] == "*":
                            cnt += 1
            matrix[i][j] = cnt
            print(matrix[i][j], end="")
        else:
            print(matrix[i][j], end="")
    print()

