
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#sum =0
#for i in range(1,1000):
#    if any([i%3 ==0, i%5 == 0]):
#        sum +=i
#print sum
        
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#check_list = [11, 13, 14, 16, 17, 18, 19, 20]
#
#def findnum(step):
#    for i in xrange(step, 999999999, step):
#        if all(i%n ==0 for n in check_list):
#            return i
#    return None 
#
#if __name__ == '__main__':
#    solution = findnum(20)
#    if solution is None:
#        print "No answer found"
#    else:
#        print "found an answer:", solution


#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#n = 600851475143 
#i =2
#while i*i < n:
#    while n%i ==0:
#        n = n/i
#        print i, n
#    i  +=1
#print n

def largestPrime(n):
    i =2
    while i*i < n:
        while n%i ==0:
            n = n/i
        i+=1
    return n

if __name__ == '__main__':
    sol = largestPrime(600851475143)
    print 'largest Prime: %d' % sol
    
    