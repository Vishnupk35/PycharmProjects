#Collect 2 number and check the largest number

num1=int(input("Enter first number:"))
num2=int(input("Enter second number"))
if(num1>num2):
    print(num1,"is greater than",num2)
elif(num2>num1):
    print(num2,"is greater than",num1)
else:
    print("Both numbers are equal")