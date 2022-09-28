lower=int(input("Please enter the lower limit number:"))
upper=int(input("Please enter the upper limit number:"))
flg=0
for i in range(lower+1,upper):
    if(upper%i==0):
        flg=1
        break
if(flg>0):
    print(i)
