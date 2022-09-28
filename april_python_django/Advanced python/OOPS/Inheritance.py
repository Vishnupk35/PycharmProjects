#Inheritance
#parent
#child
#Child class will obtain the features of parent class
#Obtain features like method and variables
#Ex, PArent A, Child B

class A:
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)

class B(A):#Inheritance, Child class, sub class, derived class
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2,self.num1)
b=B()
b.printa(60)