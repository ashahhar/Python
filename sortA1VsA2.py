# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 10:55:18 2016

@author: Rush
"""

A1= [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2= [2, 1, 8, 3]
A3=[]
A1.sort()
for i in A2:
    for j in range(0, len(A1)):
        if i ==A1[j]:
            A3.append(A1[j])
#print A3
for i in range(0, len(A1)):
    if A1[i] not in A3:
        A3.append(A1[i])
print A3