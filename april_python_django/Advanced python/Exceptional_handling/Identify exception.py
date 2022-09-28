#Identify Exception

a=[1,2,3,4]
i=int(input("Enter an index"))
try:
    print(a[i])
except Exception as e:
    print("Exception occured",e)