marklist=[]
subject =["english","math","science","marathi","history"]
n =input("enter your no of subject: ")
value =""
lists =""
for i in range(n):
    lists =raw_input("enter subject:")
    value =input("enter your marks: ")
    subject.append(lists)
    marklist.append(value)


for i in range(len(marklist)):
    total=sum(marklist)
print "your total average marks",total
    
