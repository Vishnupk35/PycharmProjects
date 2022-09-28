#Person: name,age,place
#Employee:place,phn
#Student: roll,college
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee:
    def __init__(self,place,phn):
        self.place=place
        self.phn=phn
class Student(Person,Employee):
    def __int__(self,roll,college,name,age,place,phn):
        Person.__init__(self,name,age)
        Employee.__init__(self,place,phn)
        self.roll=roll
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place,self.phn,self.roll,self.college)
ob=Student("Vishnu",24,"Alleppey",1234,35,"Luminar")
ob.printstudent()
#Single inheritance-super() [child class(parents_arguments)
#super()__init__(arguments)

#Multiple inher [classname.__init__(self,arguments)  [child [parents_argu]