num=int(input("please enter the number: "))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    if(c>=num):
        break
    print(c)

