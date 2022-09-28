# Multiple Inheritance
# Child class inherit multiple parent class

class A:
    def printa(self):
        print("Inside value is A")
class B:
    def printb(self):
        print("Inside value is B")
class C(A,B):# Multiple inheritance.
    def printc(self):
        print("Inside value is C")
ob=C()
ob.printc()
ob.printb()
