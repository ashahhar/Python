# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:31:34 2016

@author: Rush
"""

import random

def roll_again(roll_dice):
    min=1
    max=6
    roll_dice="yes"
    while roll_dice=="yes" or roll_dice=="y":
        print  random.randint(min, max)
        print  random.randint(min, max)
        roll_dice =raw_input("Roll the dice again?")
    
def countWords():
    with open('C:\Users\Rush\OneDrive\Subjects\practice\B-large-practice.in', 'r') as input:
        a=0
        for lines in input:
            k=[]
            k= lines.split(" ")
            a += len(k)
        print a

def anagram(s1, s2):
    s1=s1.replace(" ", "")
    s2 =s2.replace(" ", "")
    s1=list(s1)
    s2=list(s2)
    status= True
    if len(s1)!=len(s2):
        status = False
    else:
        s1.sort()
        s2.sort()
        if "".join(s1) !="".join(s2):
            status = False
    return status
    
def balanceParethesis(s):
    if len(s)%2 !=0:
        print "1"
        return False
        
    l =list("([{")
    main_l = ['()', '[]', '{}']
    m=[]
    for i in s:
        if i in l:
            m.append(i)
        else:
            if len(m)==0:
                return False
            endBrace = m.pop()
            if endBrace+i not in main_l:
                return False
    return True
    
    
import re
def firstRepeatedWords(s):
    s = re.findall(r'[\w]+', s)
    dict ={}
    found=None
    for word in s:
        if word in dict:
            found= word
#            return word
            break
        else:
            count =1
            dict[word]=count
    return found
    
    
#Ashely fav numbers: she likes numbers but with no repeated digits like 12, (11, 22have repeqating digits
#    so she does not like them. count thenumbers she likes from the given range.
def ashleyFavNum(i1, i2):
    c=0
#    for i in range(i1,i2+1):
#        if (i%10)!= (i/10):
#            c+=1
#    dict ={}
    for i in range(i1,i2+1):
        dict ={}
        m = len(str(i))
        print i
        for j in range(0,m):
            k =i%10
            if k in dict:
                l =dict[k]
                l+=1
                dict[k]=l
            else:
                l=1
                dict[k]=l
            i=i/10
        print c
        if len(dict)!= 1:
            c+=1
        print dict
        
    return c
        
    


if __name__=="__main__":
#    roll_again(roll_dice)
#    countWords()
#     print anagram("prime", "perim")
#    print balanceParethesis("([{}])")
#     print firstRepeatedWords("He enough had enough-of had this non-sense.")
    print ashleyFavNum(1000,1112)
    