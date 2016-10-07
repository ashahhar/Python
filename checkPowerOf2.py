# -*- coding: utf-8 -*-
"""
List three ways to check if a number is power of 2 python
"""

def check1(x):
    while(x%2==0 and x>1):
        x /=2
#        print x
    if x==1:
        return True
    else: 
        return False      
    
def check2(x):
    if any([x==1, x==2, x==4, x==8, x==16, x==32,x==64, x==128, x==256, x==512, x==1024, x== 2048, x == 4096, x == 8192, x == 16384,x == 32768, x == 65536, x == 131072, x == 262144,   x == 524288, x == 1048576,x == 2097152,   x == 4194304, x == 8388608, x == 16777216,   x == 33554432, x == 67108864, x == 134217728,   x == 268435456, x == 536870912, x == 1073741824,   x == 2147483648]):
        return True
        
def check3(x):
    onePower =1
    while(onePower <x and onePower< 2147483648):
        onePower *=2
        if onePower ==x:
            return True

def check4(x):
    if x != 0 and  not(x & (x - 1)):
        return True
    
    
    
    
if __name__ =="__main__":
    res = check4(512)
    if res:
        print "Is Power of Two"
    else:
        print "Not A Power of Two"
    