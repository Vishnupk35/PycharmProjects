# name=input("Please enter your name: ")
# print("Your name is",name)
# num1=int(input("Please enter the 1st number:"))
# num2=int(input("Please enter the 2nd number:"))
# sum=(num1+num2)
# print("The result is: ",sum)
# bootcash=2250
# if bootcash>=2000:
#     print("Your limit exceeded")
#
# else:
#     print("Your bootcash balance is:",bootcash)
num=4,7,10
ls=[]
str="skywalk"
for j in str:
    for i in range(1,len(str)+3):
        if i not in num:
            ls.append(i)
        break
    ls.append(j)



print(ls)