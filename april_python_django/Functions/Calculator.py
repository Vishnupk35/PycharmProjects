print("Select the function you want to perform\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")
choice=int(input("Please enter the choice: "))
num1=int(input("Please enter the number 1: "))
num2=int(input("Please enter the number 2: "))

def add(num1,num2):
    sum=num1+num2
    print(num1,"+",num2,"=",sum)

def sub(num1,num2):
    subtract=num1-num2
    print(num1,"-",num2,"=",subtract)

def mul(num1,num2):
    multiply=num1*num2
    print(num1,"*",num2,"=",multiply)

def div(num1,num2):
    division=num1/num2
    print(num1,"/",num2,"=",division)
if(choice==1):
    add(num1,num2)
elif(choice==2):
    sub(num1,num2)
elif(choice==3):
    mul(num1,num2)
elif(choice==4):
    div(num1,num2)
else:
    print(" Invalid input")


