#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.Print bonus
#Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Please enter your salary amount:"))
service=int(input("Please enter your year of service with the company:"))
if(service>5):
    print("Net bonus is",salary*0.05,"rs")

else:
    print("Sorry! You are not eligible to get bonus")