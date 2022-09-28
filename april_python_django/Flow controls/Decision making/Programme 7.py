# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

totalclass=int(input("Enter the total number of classes held:"))
attendance=int(input("Enter the total number of classes attended"))
if(attendance/totalclass*100>=75):
    print("You can attend the exam")
else:
    print("you can't attend the exam")