s= 'HimeshReshmiya'
l = list(s)
#print l
flag_1 =False
flag_2 =False
left =0
right = len(l)-1
for i in range(0,len(l)/2):
    if any([l[left] =='a',l[left] =='e',l[left] =='i',l[left] =='o',l[left] =='u']):
        flag_1 =True
    else:
        if(flag_1 == False):
            left +=1
    if any([l[right] =='a',l[right] =='e',l[right] =='i',l[right] =='o',l[right] =='u']):
        flag_2 = True
#        print l[right]
    else:
        if(flag_2 == False):
            right -=1
    if all([flag_1==True, flag_2==True, left<=right]):
        l[left], l[right]=l[right],l[left]
        left +=1
        right -=1
        flag_1 =False
        flag_2 =False
            
m = "".join(l)
print m