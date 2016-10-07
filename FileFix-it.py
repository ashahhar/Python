
array =[]
with open("C:\Users\Rush\OneDrive\Subjects\practice\F-large-practice.in", "r") as ins:
    for lines in ins:
        array.append(lines.strip())
length = int(array[0])
count =0
j=1
with open('op-F-py1', 'w') as f:
    for i in range(0,length):  
        temp = array[j].split(" ")
        temp=[int(k) for k in temp]
        l = temp[0]
        m = temp[1]
        count +=1
        j +=1
        dir_1 =[]
        if l>0:
            for a in range(0, l):
                tpm_1 = array[j].split("/")
                entry =''
                o =j
                for b in range(0, len(tpm_1)):
                    if tpm_1[b] !='':
                        entry += '/'+ tpm_1[b]
                        if entry not in dir_1:
                            dir_1.append(entry)
                j =o
                j+=1
        if m>0:
            cnt =0
            for a in range(0,m):
                tpm_2 = array[j].split("/")
                entry =''
                o =j
                for b in range(0, len(tpm_2)):
                    if tpm_2[b] !='':
                        entry += '/'+ tpm_2[b]
                        if entry not in dir_1:
                            cnt+=1
                            dir_1.append(entry)
            
                j=o    
                j+=1
            print "Case #%d" % count + ": %d"% cnt  
            f.write("Case #%d" % count + ": %d\n"% cnt )
    