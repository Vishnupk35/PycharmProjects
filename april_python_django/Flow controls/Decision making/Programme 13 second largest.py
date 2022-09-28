#Read 3 numbers and display the second largest number
num1=int(input("Enter 1st number:"))#100
num2=int(input("Enter 2nd number:"))#80
num3=int(input("Enter 3rd number:"))#60
#nested if
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("Second largest number is",num2)
    else:
        print("Second largest number is",num3)
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print("Second largest number is",num1)
    else:
        print("Second largest number is",num3)
elif(num3>num1)&(num3>num2):
    if(num2>num1):
        print("Second largest number is",num2)
    else:
        print("Second largest number is",num1)
else:
    print("Input is invalid")