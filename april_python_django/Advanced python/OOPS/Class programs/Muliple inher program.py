#Person: name, age
# parent: place, ph no
#employee: id, desig, salary
#Print full data
class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Parent:
    def setparent(self,place,ph):
        self.place=place
        self.ph=ph
class Employee(Person,Parent):
    def setemp(self,id,desg,sal):
        self.id=id
        self.desg=desg
        self.sal=sal
    def printemp(self):
        print(self.name,self.age,self.place,self.ph,self.id,self.desg,self.sal)
ob=Employee()
ob.setperson("Vishnu",24)
ob.setparent("alleppey",1234)
ob.setemp(2255,"developer",100000000)
ob.printemp()