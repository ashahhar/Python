def uniqueChar(s):
    k ={}    
    j =0      
    for i in s:
        if i in k:
            j +=1
            break
        else:
            m =1
            k.update({i:m})
    if j ==0:
        return '11   String has unique characters'
    else:
        return 'String has no unique characters'

def cString(s):
    s = s[::-1]
    a = "0"
    s = s + a
    print s
    return s
    
def anagram(a,b):
    c = True
    if len(a) == len(b):
        for i in a:
            if b.find(i)==-1:
                c =False
                break
                        
    else:
        return 'False'
        
    if c ==  True:
        return 'Is Anagram'
    else:
        return 'not an Anagram'
        
    
def remove_dup(string): 
    if len(string)<0:
        return "Not a String"
    if len(string)<2:
        return "Only one character"
    else:
        ans_str = string[0]
        for s in string:
            if ans_str.find(s) == -1:
                ans_str += s

    return ans_str           
            
def replaceSpace(s):
    lo= s.replace(' ', '%20')
    print lo
    print 'hello'
    a = ''
    k = list(s)
    for i in s:
        if i ==' ':
            a += '%20'
        else:
            a += i
            
    return a

def oneseven(matrix):
    '''Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column is set to 0.'''
    if not matrix:
        return matrix
    N = len(matrix)
    M = len(matrix[0])
    null_hori = set()
    null_vert = set()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                null_hori.add(i)
                null_vert.add(j)
    for i in range(N):
        for j in range(M):
            if i in null_hori or j in null_vert:
                matrix[i][j] = 0
    return matrix

def onetwo(s):
    '''Write code to reverse a C-Style String.
    (C-String means that “abcd” is represented as five characters, including the null character.)'''
    # lets pretend Python has mutable strings
    s = list(s)
    max_idx = len(s) - 1
    for i in range(len(s)/2):
        t = s[i]
        s[i] = s[max_idx - i]
        s[max_idx - i] = t
    return ''.join(s)

def oneeight(s1, s2):
    print len(s1)==len(s2) and s1 in 2*s2
    return s1 in s1+s2
    
if __name__== '__main__':
#    s1 = uniqueChar('aabcdefhgtrithj')
#    print s1
#    s2 = cString('abcd')
#    print s2
#    print remove_dup("gsagyxgdhycgdgxcgsfxgsfxuhsugy")
#    print anagram('iceman','cinema' )
#    print replaceSpace('there is a cow')
#    matrix = [[1,2,1], [4,0,6], [7,8,9] ]
#    print oneseven(matrix)
#    k = onetwo('abc')
#    print len(k)
#    print oneeight('waterbottle', 'erbottlewat' )