'''
Inheritance: Acquiring the properties of ancestor class/es

1.Multi level inheritance - one by one
2.Multiple Inheritance - more than one at a time
'''
class GrandFather:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(f"this is grandfather constructor {name} age of{age}")
        
    def gf_method(self):
        print("This is GF method")

class Father(GrandFather): #properties of gf class is inherited to father class
    
    def __init__(self, aadhar_id):
        super().__init__(name, age)
        self.aadhar_id=aadhar_id
        print(f"this is father constructor {self.name} age of {self.age} id is {self.aadhar_id}")
        
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")   
        
class Mother:
    def m_method(self):
        print("This is Mother method")
        
    def car(self):                    #same name us given in both mother and father(car) but it will print father car  because in child class (father,mother)you initialize father first
        print("This is Mother's car")   
        
class Child(Father, Mother):           #Multiple Inheritance
    def c_method(self):
        print("this is child")
        
obj1=GrandFather("ajja", "90") 
# obj1.gf_method()  

obj2=Father("appa", 60, 467)
# obj2.f_method()
# obj2.gf_method() #calling gf property from father objects  
     
obj3=Child("me", 12, 567)
# obj3.gf_method()
# obj3.f_method()
# obj3.car()
# obj3.c_method()
# obj3.m_method()  

print(Child.mro()) #method resolution order (to check the order)