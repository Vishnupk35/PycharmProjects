#1. create a list from element of a range from 1200 to 2000 with steps of 130
#2. lst=[44,54,64,74,104] create a new list from this lst1=[50,60,70,80,110
#3. 1,15 elements square greater than 50 print

lst0=[i for i in range(1200,2000,130)]
print(lst0)

lst=[44,54,64,74,104]
lst1=[i+6 for i in lst]
print(lst1)

lst2=[i for i in range(1,16) if i**2>50]
print(lst2)
