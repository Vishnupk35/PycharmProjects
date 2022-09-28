#tuple *args
#kwargs : Key word arguments
#denoted by **args
#We can add keys or head to the values read.
def printvalue(**args):
    return args

print(printvalue(id=101,name="Vishnu",age=24,place="Thuravoor",prof="Developer"))