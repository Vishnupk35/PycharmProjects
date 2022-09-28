
class Employee1:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printinfo(self):
        print(self.name,self.age,self.place)
f=open("Employee_data","r")
for i in f:
    data = i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    place=data[2]
    ob=Employee1(name,age,place)
    ob.printinfo()
