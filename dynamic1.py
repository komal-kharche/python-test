roll_no=[]
subject=[]
marklist=[]
n = input("no of student list:")
num =""
lists=""
value=""
for i in range(n):
    num =input("enter your roll no: ")
    lists =raw_input("enter your favoruit subject: ")
    value = raw_input("enter your marks: ")
    roll_no.append(num)
    subject.append(lists)
    marklist.append(value)

for i in range(len(roll_no)):
    print "roll no",roll_no[i],"of there favoruit subject is",subject[i],"and their marks is",marklist[i]
    
