# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 20:12:20 2016

@author: Rush
"""
from collections import OrderedDict
ip="Careercup is a good site . Careercup provides a lot of information ."
ipdict=OrderedDict()
iplist=ip.split(" ")
for i in iplist:
    if ipdict.has_key(i):
        ipdict[i]+=1
    else:
        ipdict[i]=1
#print ipdict
for i in ipdict:
    if ipdict[i]==1:
      #  print i
        break
    
    
def topUsers(s, k):
    c={}
    for i in s:
        if i in c.keys():
            j=c.get(i)
            j +=1
            c[i]=j
        else:
            j=1
            c.update({i: j})
    for key in c:
        value =c[key]
        if(value >=2):
            print key +" ", value

##Write a method that combines an array of iterators into a new one, such that, e.g. for input [A B C] where: 
#A.next() returns a1, a2, respectively; 
#B.next() returns b1; 
#C.next() returns c1, c2, c3, respectively; 
#The new iterator will return elements in this order: a1 b1 c1 a2 c2 c3.
##
def combine(A, B, C):
    k = max(len(A), len(B), len(C))
    i=0
    newL=[]
    while(len(C)>0):
        if len(A)!=0:
            newL.append(A[i])
            del A[i]
        if len(B)!=0:
            newL.append(B[i])
            del B[i]
        if len(C)!=0:
            newL.append(C[i])
            del C[i]
    print newL

#Write a program to modify the string in following pattern, 
#Change odd words to uppercase and Reverse the even words. Make sure that the spaces (multiple) between the words remains as it is. 
#E.g.: 
#Input : "This is a test String!!" 
#Output: "THIS si A tset STRING!!"
def changePattern(Input):
    l= Input.split(" ")
    for i in range(0, len(l)):
        if i%2 ==0:
            l[i]=l[i].upper()
        else:
            str =l[i]
            l[i]=str[::-1]
    print ' '.join(l)
      
import math
def perfectSquares(new_ip):
    k= int(new_ip[0])
    new_l =[]
 #   range1 = lambda start, end:(start, end+1)
    for i in range(1, len(new_ip)):
        m = new_ip[i].split(" ")
        c =0
        for j in range(int(m[0]), int(m[1])+1):
            if math.sqrt(j) - int(math.sqrt(j)) ==0:
                c +=1
        new_l.append(c)       
    return new_l

def checkPalin(pa):
    ma = pa[::-1]
    if ma==pa:
        return "Is a Palindrome"
    else:
        return "Not a Palindrome"

if __name__ =="__main__":
    s=["user1", "user4", "user2", "user1", "user3", "user1", "user2", "user3"]
    k=2
   # topUsers(s, k)
    A =["a1", "a2"]
    B =["b1"]
    C =["c1", "c2", "c3"]
  #  combine(A, B,C)
    
    Input = "This is a test String!!" 
    #changePattern(Input)
    
    ip =  open("E:\\Courses\\Python\\1.txt", "r") 
    new_ip =[]
    for line in ip:
        new_ip.append(line)
    lst = []
    #lst = perfectSquares(new_ip)
#    for i in lst:
#        print i
        
    pa ="A man, a plan, a canal, Panama"
    ansPa = checkPalin(pa)
#    print ansPa
    
    