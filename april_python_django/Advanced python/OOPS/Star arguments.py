#*arguments(*args)(*argumentname)

# def printvalue(num1,num2):
#     print(num1,num2)
# #printvalue(10,20)
# printvalue(10,20,30)#printvalue() takes 2 positional arguments but 3 were given

#*args is used to avoid the above error. We can provide n number of arguments without predefining it.

def printvalue(*num):
    print(num)

printvalue(10,20,30,5,6,7,7,8,2,56,7) #Result will be in Tuple format





