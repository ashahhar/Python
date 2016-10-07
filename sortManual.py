# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 18:55:04 2016

@author: Rush
"""

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
lst =[]

for i in range(0, len(data_list)-1):
    for j in range(i+1, len(data_list)):
        temp=0
        if data_list[i]< data_list[j]:
            data_list[i], data_list[j]=data_list[j], data_list[i]
print data_list