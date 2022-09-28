#Person: name,age
#Child: place,school
#Student: roll,dept,college
#print: name,age,place,dept,college
class Person:
    def setperson(self,name, age):
        self.name=name
        self.age=age
class Child(Person):
    def setchild(self,place,school):
        self.place=place
        self.school=school
class Student(Child):
    def setstudent(self,roll,dept,college):
        self.roll=roll
        self.dept=dept
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place,self.dept,self.college)#name,age,place,dept,college

ob=Student()
ob.setperson("Vishnu",24)
ob.setchild("Aleppey", "TD")
ob.setstudent(35,"Python","Luminar")
ob.printstudent()