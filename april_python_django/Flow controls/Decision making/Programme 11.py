#read 4 subjects marks
#Total marks above 180- A+
#160-179 - A
#140-159 - B+
#120-139 - B
#100-119 - C+
#80-99 - C

mark1=int(input("Enter marks of Subject 1 out of 50: "))
mark2=int(input("Enter marks of Subject 2 out of 50: "))
mark3=int(input("Enter marks of Subject 3 out of 50: "))
mark4=int(input("Enter marks of Subject 4 out of 50: "))
SUM=mark1+mark2+mark3+mark4
if(SUM>180)&(SUM<=200):
    print("Your grade is A+")
elif(SUM>=160)&(SUM<180):
    print("Your grade is A")
elif(SUM>=140)&(SUM<160):
    print("Your grade is B+")
elif (SUM>= 120) & (SUM < 140):
    print("Your grade is B")
elif(SUM>=100)&(SUM<120):
    print("Your grade is C+")
elif(SUM>=80)&(SUM<100):
    print("Your grade is C")
else:
    print("Sorry! You are failed")