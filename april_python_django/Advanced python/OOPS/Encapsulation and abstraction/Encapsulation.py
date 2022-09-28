#Encapsulation
#wrapping of data

class Person:
    def __init__(self):
        self.name="Vishnu"#Pubic
        self.id=35#Public
        self.__password=12345#Private (We cannot access this data unless we create a function to print this data)
        self._age=24 #Protected (We can access this data inside the class or from a class which inherit this)
    def setvalue(self,name,id):
        self.name=name
        self.id=id
    def readvalue(self):
        print(self.name,self.)


