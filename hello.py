s= 'HimeshReshmiya'
l = list(s)
m = iter(s)
length=0
count =0
i=0
try:
    while(m.next() != None):
        length +=1
        i+=1
        if(length%2 == 0):
            count +=1
except StopIteration:
    pass
print 'Middle Character: %s' % (l[count])
    