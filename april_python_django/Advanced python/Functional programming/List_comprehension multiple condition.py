#SYNTAX
#Elif will not use here. Instead of that use if iteself.
#list_name=[print if condition else print range]

# If number is even print the sqaure else printe cube. 1-50
lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)