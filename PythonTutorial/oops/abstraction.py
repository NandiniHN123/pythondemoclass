'''
Abstraction

Interface: as an abstract class containing abstract method only

all interfaces are abstract class but all abstract class are not interfaces
#abstract class can have one or more abstract method
'''

'''
from abc import ABC, abstractmethod   #small abc -module, ABC class
class Car(ABC):
    def no_of_wheels(self):  # implemented method
        print("Car has 4 wheels")
        
    @abstractmethod   #decorator #abstract class can have one or more abstract method
    def no_of_seats(self):   #unimplemented  method
        pass
        
class SUV(Car):
    def no_of_seats(self):
        print("car has 8 seats")
    
    def display_suv(self):
        print("This is SUV car")
        
duster=SUV()
duster.display_suv()
duster.no_of_seats()
'''
from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self):
        print("welcom")
    @abstractmethod
    def size(self):
        pass
        
class Bhaskar:
    def __init__(self):
        print("Bhaskar:",end=" ")
        
    def size(self):
        print("king size")
        
        
class Classmet:
    def __init__(self):
        print("classmet")
        
    def size(self):
        print("long")
        
class vidya:
    def __init__(self):
        print("vidya")
        
    
        
b1=Bhaskar()
b1.size()

b2=vidya()
        
    
