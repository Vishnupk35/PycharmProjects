# num1=int(input("Enter a number: "))
# num2=int(input(" Enter 2nd number: "))
# print(num1/num2)
#6/0 will get error, it's a unexpected error. It's an error caused from input
# Exceptional handling is the method to avoid unexpected errors.

# Three blocks are used in exceptional handling.
#try (blocks which may have a chance to get an unexpected error)
#except(solution for the exception added here)
#finally(same like pass, will work even there is exception or not)
num1=int(input("Enter a number: "))
num2=int(input(" Enter 2nd number: "))
try:
    print(num1/num2)
except:
    print("Zero  division error")
finally:
    print("Great")



