class Person:
    def __init__(self,id,fname,lname,age,prof,country):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.country=country
    def printdata(self):
        print(self.id,self.fname.self.lname,self.age,self.prof,self.country)

f=open("C:/Users/v-kvis/Downloads/customer","r")
lst=[]
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    country=data[-1]

    ob1=Person(id,fname,lname,age,prof,country)
    #fname,lname,age,prof
    lst.append((ob1.fname,ob1.lname,ob1.prof))
    print(lst)