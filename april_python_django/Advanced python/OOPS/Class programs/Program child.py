#Create 2 class and print values from Class person to class student.

#Person: name age place
#Student: roll, dept
class Person:
    def setval(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        # print(self.name,self.age,self.place)
    def printval(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def setstu(self,roll,dept):
        self.roll=roll
        self.dept=dept
    def printstu(self):
        print(self.name,self.age,self.place,self.roll,self.dept)

st=Student()
st.setval("Vishnu",24,"Alappuzha",)
st.setstu(35,"Python")
st.printstu()