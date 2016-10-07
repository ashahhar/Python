array=[]
with open("C:\Users\Rush\OneDrive\Subjects\practice\A-large-practice.in", "r") as ins:
    for line in ins:
        array.append(line.strip())
t  = len(array)
count =0
j=1

with open('op-A-py1', 'w') as f:
    for i in range(0,t-1):
        while j<t-2:
            temp1 = int(array[j])
            j+=2
            temp2 = array[j].split()
            for l in xrange(len(temp2)):
                for m in xrange(l+1,len(temp2)):
                    if int(temp2[l])+int(temp2[m]) == temp1:
                        count +=1
                        a = temp2.index(temp2[l])+1
                        b = temp2.index(temp2[m])+1
                        if a == b:
                            indices = [i for i, x in enumerate(temp2) if x == temp2[l]]
                            a= (indices[0]+1)
                            b = indices[1]+1
                            f.write("%s\n" % str('Case #%d' % count +': %d'  % a + ' %d' % b))
                            print 'case # %d' % count +'  %d'  % a + ',   %d' % b
                            continue
                        if a<b:
                            f.write("%s\n" % str('Case #%d' % count +': %d'  % a+ ' %d' % b))
                            print 'case # %d' % count +'  %d'  % a + ',   %d' % b
                        else:
                            f.write("%s\n" % str('Case #%d' % count +': %d'  % a + ' %d' % b))
                            print 'case # %d' % count +'  %d' % a + ',   %d' % b
                    
            j +=1
            i=j
#f.closeS