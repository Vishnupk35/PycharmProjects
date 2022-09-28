#Collect 3 number and check the largest number

num1=int(input("Enter first number:"))#100
num2=int(input("Enter second number"))#80
num3=int(input("Enter third number"))#60
if(num1>num2)&(num1>num3): #100>80 - 1, 100>60- 1 = 1
    print(num1,"is greater than",num2,"and",num3)
elif(num2>num3)&(num2>num1):
    print(num2,"is greater than",num3,"and",num1)
else:
    print(num3,"is greater than",num2,"and",num1)
