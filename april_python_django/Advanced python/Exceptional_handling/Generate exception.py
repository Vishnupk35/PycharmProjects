
#How to generate exception
#Syntax (raise Exception("content to print")

age=int(input("Please enter your age: "))
if age>=18:
    print("Congrats! You are eligible")
else:
    raise Exception("not eligible")