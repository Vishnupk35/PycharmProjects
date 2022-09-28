#Person: name, age, place
#Student: roll no,dept,college(Child of person)
#print

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll,dep,col,name,age,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dep=dep
        self.col=col
    def printstvalue(self):
        print(self.roll,self.dep,self.col)

ob=Student("Vishnu",24,"Alleppey",35,"python","Luminar")
ob.printstvalue()
ob.printvalue()