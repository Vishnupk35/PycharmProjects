lower=int(input("please enter the upper limit number:"))
upper=int(input("please enter the upper limit number:"))
evensum=0
oddsum=0
for i in range(lower,upper+1):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print(evensum)
print(oddsum)