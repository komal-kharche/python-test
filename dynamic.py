name = []
marks = []
n =input("number of student are comming: ")
value =""
sheets =""
for i in range(n):
    value = raw_input("enter your name: ")
    sheets =raw_input("enter your marks: ")
    name.append(value)
    marks.append(sheets)

for i in range(len(name)):
    print name[i],"as got",marks[i]
    
    if 35 < marks:
        print name[i],"are eligible"
    else:
        print name[i],"are not eligible"
        
    
