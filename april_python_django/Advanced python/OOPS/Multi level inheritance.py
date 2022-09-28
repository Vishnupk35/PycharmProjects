#Multi level inheritance

class A:
    def seta(this):
        print("Inside A")
class B(A):
    def setb(this):
        print("Inside B")
class C(B):
    def detc(self):
        print("Inside C")
ob=C()
ob.detc()
ob.setb()