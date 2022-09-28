#Display road tax to be paid

# Cost
# price( in Rs)                                       Tax
# > 100000
# 15 %
# > 50000 and <= 100000
# 10 %
# <= 50000
# 5 %

bikecost=int(input("Enter the cost of bike"))
if(bikecost>100000):
    print("The tax amount required to pay:",bikecost/100*15)
elif(bikecost<50000):
    print("The tax amount required to pay:",bikecost/100*5)
else:
    print("The tax amount required to pay:", bikecost/100*10)
