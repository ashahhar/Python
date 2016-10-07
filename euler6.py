import numpy as np


def Sum_Square_Difference(step):
    cntsq =0
    cntnum =0
    for i in xrange(step+1):
        cntsq += i*i
        cntnum += i
    diff = (cntnum * cntnum) - cntsq
    return diff
    
def even_febonacci_number(limit):
    val=0
    num = 1
    count=0
    a =[]
    sum =0
    while sum <= limit:
       sum = val + num
       val = num
       num = sum
       a.append(sum)
       if sum%2==0:
           count +=sum
    print a    
    return count
          
def largest_pallindrome(start, end):
    a =[]
    for i  in range(start, end,-1):
        for j in range(start, end,-1):
#            print j
            k = i*j
#            print k
            if str(k) ==str(k)[::-1]:
#                print i, j
#                return k
                a.append(k)
    return np.amax(a)
    
def pallindrom(start, end):
    for i in range(start, end, -1):
        k =i
        product = k*i
        if str(product)==str(product)[::-1]:
            print '1st: %d ' % k +'2nd %d' % i
            return product
        else:
            k =i-1
            product = k*i
            if str(product)==str(product)[::-1]:
                print '1st: %d ' % k +'2nd %d' % i
                return product

def palin(num):
    k = str(num)[::-1]
    return int(str(num)+str(k))
    
def large_palindrome(start, end):
    found = False
    j = start
    while found == False:
        j -=1
        k =palin(j)
        for i in range(start, end, -1):
            if any([k/i >start , i*i<k]):
                break
            if k%i == 0:
                found =True
                print '1st Number: %d' % (k/i)
                print '1st Number: %d' % (i)
                return k
                break
            
            

def eighttwo(N, offlimits=None):
    '''
    Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
    only move in two directions: right and down. How many possible paths are there for
    the robot?
    FOLLOW UP
    Imagine certain squares are “off limits”, such that the robot can not step on them.
    Design an algorithm to get all possible paths for the robot.
    '''
    paths = []
    def walk(x, y, path=None):
        if x >= N or y >= N:
            return
        if (x,y) in offlimits:
            print offlimits
            return
        if path is None:
            path = []
        path = path[:]
        path.append((x,y))
        if x == N - 1 and y == N -1:
            paths.append(path)
            
        walk(x+1, y, path)
        walk(x, y+1, path)
    if offlimits is None:
        offlimits = []
    offlimits = set(offlimits)
    walk(0, 0)
    print len(paths)
    return paths

def eightfour(s):
    '''Write a method to compute all permutations of a string.'''
    if len(s) <= 1:
        return [s]
    if len(s) == 2:
        return [s, s[::-1]]
    permuts = eightfour(s[:-1])
#    print permuts
    result = []
    for p in permuts:
        for i in range(len(p)+1):
            result.append(p[:i] + s[-1] + p[i:])
#    print len(result)
#    print result
    return result

def eightfive(N):
    '''
    Implement an algorithm to print all valid (e.g., properly opened and closed) combi-
    nations of n-pairs of parentheses.
    EXAMPLE:
    input: 3 (e.g., 3 pairs of parentheses)
    output: ()()(), ()(()), (())(), ((()))
    '''
    def walk(s, l, r):
        if l > 0:
            walk(s + '(', l-1, r)
        if r > l:
            walk(s + ')', l, r-1)
        if not l and not r:
            print s
    walk('', N, N)
    

def find_ways(money,denom):
    next_denom=0
    while denom>0:
        if denom==25:
            next_denom=10
            break
        elif denom==10:
            next_denom=5
            break
        elif denom==5:
            next_denom=1
            break
        elif denom==1:
            return 1        
    ways=0
    i=0
    while i*denom<=money:
        ways +=find_ways(money-i*denom,next_denom)
        i=i+1
    return ways

   
if __name__ == '__main__':
#    s1 = Sum_Square_Difference(100)
#    print 'difference: %d' %s1
#    s2 = even_febonacci_number(4000000)
#    print 'Sum of Even numbers in Fibonacci: %d'   % s2
#    s3 = largest_pallindrome(999,99)
#    print 'Largest palindrome: %d' %s3
#    s4 = pallindrom(999,99)
#    print 'Largest palindrome: %d' % s4
#    s5 = large_palindrome(999, 99)
#    print 'Largest palindrome: %d' % s5
#    print eighttwo(4)
    print eightfour('Hello')
#    print eightfive(3)
#    print find_ways(50,25)



    


