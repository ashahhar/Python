# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 14:21:26 2016

@author: Rush
"""
def largeProductPair(a1):
    a1.sort()
    a3=0
    a4=[]
    for i in range(0, len(a1)-1):
        m = a1[i]*a1[i+1]
        if m>a3:
            a3 =m
            if len(a4)==0:
                a4.append(a1[i])
                a4.append(a1[i+1])
            else:
                a4[0], a4[1]=a1[i], a1[i+1]
    print a4   



if __name__=="__main__":
    a1 = [1, 4, 3, 6, 7, 0]
    a2 = [-1, -3, -4, 2, 0, -5]
    largeProductPair(a2)