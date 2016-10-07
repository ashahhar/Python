
array =[]
with open("C:\Users\Rush\OneDrive\Subjects\practice\C-large-practice.in", "r") as ins:
    for lines in ins:
        array.append(lines.strip())
print len(array)-1
count =0
j=2
temp =[]
with open('op-C-py1', 'w') as f:
    for i in range(2,100  ):    #len(array)-1   
        if j<len(array)-1:
            temp=(array[j].split(" "))
            new_temp = [int(k) for k in temp]
            j+=1
            temp=(array[j].split(" "))
            new_t = [int(k) for k in temp]
            new_temp.extend(new_t)
            new_temp.sort()
#            print new_temp
            count += 1
            a=1
            add =0
            for l in range(0,len(new_temp)):
                if l < ((len(new_temp)/2)):
                    add += new_temp[l]*new_temp[len(new_temp)-a]
#                    print new_temp[l], new_temp[len(new_temp)-a]
                    a+=1
            print "Case #%d" % count +": %d" % add
            f.write("Case #%d" % count +": %d\n" % add)
            j +=2
            i=j
        

