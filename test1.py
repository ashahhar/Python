
array =[]
with open("C:\Users\Rush\OneDrive\Subjects\practice\F-large-practice.in", "r") as ins:
    for lines in ins:
        array.append(lines.strip())
length = int(array[0])
count =0
j=1
with open('op-F-py1', 'w') as f:
    for i in range(0,9):  
        temp = array[j].split(" ")
        temp = [int(k) for k in temp]
        j+=1
        chk = temp[1]
        for l in range(0, temp[0]):
            tmp1 = array[j]
            
            
     
            print "Case # %d" % count + ": %d" % cnt  
            f.write("Case #%d" % count + ": %d\n"% cnt )
    