class A:
    def printa(self):
        print("Inside Class A")
class B(A):
    def printa(self):
        print("Inside Class B")
class C(B):
    def printa(self):
        print("Inside Class C")
ob=C()
ob.printa() #Inside Class C will be printed here because it's the child class.
