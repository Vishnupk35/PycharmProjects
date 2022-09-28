#Functional programming
#1. Function without arguments and no return type
#2. Function with arguments and no return type
#3. Function with arguments and return type


#Function with arguments and return type

# def add(num1,num2):
#     sum=num1+num2
#     return sum
# data=add(10,20)
# print(data)
#5 lines in the above method and it is traditional method.
# To reduce length of code we use functional programming.
#1. lambda function.
# It's an anonymous function. (No Identity)

#SYNTAX
# variable_name=lambda arguments:operation
#Multiplication example
# f=lambda num1,num2,num3:num1*num2*num3
# print(f(2,5,10))

#Find cube of a number
# f=lambda num1:num1**3
# print(f(5))

#2. Map

#SYNTAX
#variable_name=list(map(argument1,argument2))
#argument1===> function
#argument2===> iterable(From where we need to use data)

# lst=[1,2,3,4,5,6,7,8,9,10]

# def square(num):
#     res=num**2
#     return res
# data=list(map(square,lst))
# print(data)

#or
# data=list(map(lambda lst:lst**2,lst))
# print (data)
#Example add 1 to each values in list

# lst=[1,2,3,4,5,6,7,8,9,10]
# data=list(map(lambda lst:lst+1,lst))
# print(data)


#3. Filter
#SYNTAX
#variable_name=list(filter(argument1,argument2))

