#Jumping
#Jum

#break: To exit from the loop
#continue:To skip the condition from loop
#pass:Do nothing (It can be used if we want don't want perform a condition)

#continue
# for i in range(1,51):
#     if(i==25):
#         continue
#     print(i)
#     Result: 25 will not be printed except other numbers.

#pass
#1,50 even numbers pass and print the odd numbers square
for i in range(1,51):
    if(i%2==0):
        pass
    else:
        print(i**2)