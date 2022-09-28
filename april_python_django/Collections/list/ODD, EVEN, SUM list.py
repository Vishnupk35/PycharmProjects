lst=[]
lsteven=[]
lstodd=[]
for i in range(1,101):
    lst.append(i)
    if(i%2==0):
        lsteven.append(i)
    else:
        lstodd.append(i)
print(lst)
print(lstodd)
print(lsteven)
print("Sum of all numbers in lst ",sum(lst))
print("Sum of odd numbers is ",sum(lstodd))
print("Sum of even numbers is ",sum(lsteven))