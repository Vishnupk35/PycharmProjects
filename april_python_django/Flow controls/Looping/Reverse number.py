#print reverse of 153
num=int(input("please enter the number"))
res=0
while(num!=0):
    dig=num%10#153%10=3
    res=(res*10)+dig
    num=num//10
print(res)