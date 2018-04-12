name = []
n = 10
value=""
for i in range(n):
    value =raw_input("enter your name: ")
    name.append(value)

for i in range(len(name)):
    print "my name is",name[i]

print "all students name added successfully"
