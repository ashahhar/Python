
#import random
#k = "abcdefghijklmnopqrstuvwxyz"
#k =list(k)
#print k
#s =""
#for i in range(0, 21):
#    s+=k[random.randint(0,len(k))]
#print s


def panagram(st):
    alphabets ='abcdefijklmnopqrstuvwx'
    print st
    st.lower()
    print st
    st =list(st)
    status = True
    for char in alphabets:
        if char not in st:
            print char
            status=False
            break
    return status
    
def reverseLine(st):
    st = st.lower();
    st = st.split(" ")
    b=''
    for i in range(len(st)-1, -1,-1):
        a=''
        for j in range(len(st[i])-1,-1,-1):
            a+=st[i][j]
        b +=a+" "
    st =b.title()
        
    return st
    
def removeDuplicates(st):
    st = st.lower()
    st = st.split("|")
    st 
    s = st
#    print s
#    print st
    for i in st:
        print i
    
      
if __name__ =="__main__":
#    print panagram('We promptly judged antique ivory buckles for the next prize ')
    print reverseLine("Thou art thyself though not a Montague - from Romeo and Juliet")
#    print "IBM cognitive computing|IBM /cognitive/ computing is a revolution| ibm cognitive  computing|/IBM Cognitive Computing/ is a revolution?"
    removeDuplicates("IBM cognitive computing|IBM /cognitive/ computing is a revolution| ibm cognitive  computing|/IBM Cognitive Computing/ is a revolution?")