#List_comprehension

# To reduce length of program
# Example showed below (Add 1 to 100 to a new list)
# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)

#SYNTAX1
# listname=[print range]
#print ===> what to print
# lst=[i for i in range(1,101)]
# print(lst)

#Problem1 print 1 to 75 with 4 increment
# lst=[i for i in range(1,76,4)]
# print(lst)
#problem2 print 1 to 100 even numbers
#SYNTAX 2 (Only 1 condition)
# listname=[print range condition]

# lst=[i for i in range(1,101) if i%2==0]
# print(lst)

#Problem 3 print 1 to 50 odd numbers
# lst=[i for i in range(1,51) if i%2!=0]
# print(lst)

#Problem 4 print if number is even from 1 to 50

lst=[(i,"even") for i in range (1,51) if i%2==0]
print(lst)