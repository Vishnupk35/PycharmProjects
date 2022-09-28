#Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

num=int(input("Please enter the number:"))
if(num%5==0):
    print("Hello")
else:
    print("Bye")