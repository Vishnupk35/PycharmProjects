#Polymorphism
#Different methods but same name
#methods
#method overloading
#method overriding
class A:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class B:
    def sum(self, num1, num2,num3):#Same method name but different methods
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+)