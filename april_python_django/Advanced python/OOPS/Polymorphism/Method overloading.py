class A:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class B(A):
    def sum(self, num1, num2,num3):# Will work this because doesn't support method overloading. So it will read latest one.
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
ob=B()
ob.sum(5,6,8)#will execute latest menthod in python