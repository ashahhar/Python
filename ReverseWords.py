
array =[]
with open("C:\Users\Rush\OneDrive\Subjects\practice\B-large-practice.in", "r") as ins:
    for lines in ins:
        array.append(lines.strip())
        
print len(array)
count =0
with open('op-B-py2', 'w') as f:
    for i in range(1,len(array)):
        temp = array[i].split(" ")
        s=""
        count +=1
        for j in range((len(temp)-1), -1, -1):
            s += (temp[j] + " ")
        print "Case #%d" % count + ": %s " % s
        f.write("Case #%d" % count + ": %s\n" % s)
        

