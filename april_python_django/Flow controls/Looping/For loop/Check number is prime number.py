num=int(input("Please enter the number:"))#5
flg=0
for i in range(2,num):
    if(num%i==0):
        flg=1
        break
if(flg>0):
    print("Hello,",num, "is a not prime number")

else:
    print("Hello,",num,"is a prime number")
