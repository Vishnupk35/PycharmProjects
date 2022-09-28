#3. given input # find whether it is a prime or not

num=0
num1=10
flg=0
flg2=0
for i in range(num+2,num1):
    if (num1%i==0):
        flg+=1
        print(i)
    else:
        flg2+=1
print(flg)
print(flg2)




