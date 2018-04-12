num = [1,3,2,5,7,6,4,9,8,0,12,34,55,13,57,29]

for i in range(len(num)):
    a = num[i] % 2
    if a == 0:
     print "the number is even",num[i]
    else:
     print"the number is odd",num[i]

print"odd even number are separated"
