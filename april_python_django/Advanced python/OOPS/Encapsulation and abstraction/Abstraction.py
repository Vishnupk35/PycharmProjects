#abstraction
#Abstract class is called abstract class if there is atleast 2 abstract methods
#Child classes should maintain the template given in parent class
from abc import ABC, abstractmethod
class Vehicle:#Abstract
    @abstractmethod
    def Tyre(self):#abstract function
        pass
    @abstractmethod
    def Engine(self):
        pass
    @abstractmethod
    def Speed(self):
        pass
class Car(Vehicle):
    def Tyre(self):
        return 155
    def Engine(self):
        pass

    def Speed(self):
        pass
ob=Car()
print(ob.Tyre())
