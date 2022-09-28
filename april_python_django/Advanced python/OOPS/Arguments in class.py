class Person:
    def setvalue(self,name,age,place):#name age and place are arguments.#Method1
        self.name=name  #self.instantselfname=argument( Changed to instant keyword here)
        self.age=age
        self.place=place#self is the instant keyword used to convert the arguments to an instant keyword. Then only we can use the same value
#of one argument in a different one.

    def printvalue(self):#Method 2
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("anu",25,"Kochi")
pe1.printvalue()#Will print the values assigned to pe1 reference.

pe2=Person()
pe2.setvalue("Vishnu",24,"Alappuzha")
pe2.printvalue()
