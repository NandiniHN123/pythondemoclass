'''
Encapsulation:

example: class is a capsule (it holds methods and variables inside) the process is called encapsulation

Access modifiers:
1. Public properties (it can access from any where)
2. Protected: _, before variable name (this can be access only inside the class and its sub class)
3. Private: __, can be access only inside the class
'''
'''
class CarClass:
    
    company="abc"   
    
    def __init__(self,name, roll_no):
        self._name=name              # protected variable
        self.__roll_no=roll_no      #Private variable  #we can't access it outside the class(ex:car1. option no shows) 
        
    def display_details(self):
        print(f"{self.name} Car is created for {CarClass.company} company ")
  
    def move_forward(self,speed):         
        print(f"{self.name} Car is moving forward at {speed} kmph ")   
class Ndn:
    def hn(self):
        print("yes")
    
    
car1=CarClass("abc", 121)
print(car1._name)
print(car1._CarClass__roll_no)    #indirectly accessing the private properties
car1._name
    
#print(dir(car1))
'''

class person:
    def __init__(self,name,ph_no,ac_no):
        self.name=name
        self._ph_no=ph_no
        self.__ac_no=ac_no
        # print(f"{self.name} {self._ph_no} {self.__ac_no}")
        
        
p=person("nandu", 87879, 9008978)
print(p.name)
print(p._ph_no)
print(p._person__ac_no)
        

