#Constructor
#Is used to define instance variable in Object

class Person:
    def __init__(self,name,age,place):#Constructor
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=Person("Vishnu",24,"Aleppey")#Defined instance variable
pe1.printvalue()