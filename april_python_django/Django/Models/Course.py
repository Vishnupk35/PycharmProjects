class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course")
        self.status=kwargs.get("status")

    @property
    def get_name(self):
        print(self.course_name)
        return self.course_name
    def __str__(self):
        return self.course_name
class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self,**kwargs):
        return self.batch_code
    # def active_status(self):
    #     return self.active_status

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course="django",status=True)
ms=Course()
ms.add_course(course="mearn stack",status=True)
bd=Course()
bd.add_course(course="bigdata",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22",start_date="12-6-2022")
print(djb1.course.get_name)

rahul=Student()
rahul.add_student(student_name="rahul",email="rahul@gmail.com",batch=djb1)

akhil=Student()
akhil.add_student(student_name="akhil",email="akhil@gmail.com",batch=djb1)

vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu@gmail.com",batch=djb1)

msb1=Batch()
msb1.add_batch(course=ms,batch_code="msmay2k22",start_date="12-7-2022")

prajith=Student()
prajith.add_student(student_name="prajith",email="prajith@gmail.com",batch=msb1)

jijomon=Student()
jijomon.add_student(student_name="jijomon",email="jijomon@gmail.com",batch=msb1)

students=[]
students.append(rahul)
students.append(akhil)
students.append(vishnu)
students.append(prajith)
students.append(jijomon)

#print students in mearn stack
ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="mearn stack"]
print(ms_stud)