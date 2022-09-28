#name,roll,age,instituition,fees
#create 3 objects
class Luminar:
    inst="Luminar"
    fees="30000"
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.inst,Luminar.fees)
st1=Luminar()
st1.setvalue("Vishnu",35,24)
st1.printvalue()

st2=Luminar()
st2.setvalue("Arun",50,35)
st2.printvalue()

st3=Luminar()
st3.setvalue("Hari",34,33)
st3.printvalue()
