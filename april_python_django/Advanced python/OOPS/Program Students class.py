class Student:
    def read(self,name,rollno,department,college_name):
        self.name=name
        self.roll=rollno
        self.dept=department
        self.colg=college_name
    def printvalue(self):
        print(self.name)
        print(self.roll)
        print(self.dept)
        print(self.colg)
pe1=Student()
pe1.read("Vishnu",35,"Python","Luminar")
pe1.printvalue()