#Method Overriding.

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("Inside class A",self.num1+self.num2)
class Add2(Add):
    def sum(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print("Inside class B",self.no1+self.no2)

#Overiding- Same method name and same number of arguments.
#Child class will be working in this case.
#Child class overwrite the parent class.

ob=Add2()
ob.sum(15,20)
