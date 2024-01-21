'''
continuation of constructor (__init__)
constructors - is use for initializations that are required during the object creation(while creating the object we use constructor
                 as initializer to initialize that object with specific characteristics

Def- Constructor is a method used to initialize instance/object variables   
            
1.Constructor is not mandatory
2.Constructor will be called implicitly by default as soon as an object is created 
3.We can call constructor explicitly if required    
4.Constructor can be parameterized or non-parameterized   
         
'''
class Student:
    def __init__(self):     # self represents the object of the class
        print("This is student class constructor")
        
    def message(self):
        print("I'm a student")
        
std1=Student() # 0/p this is student class constructor( here i'm not calling but it will print o/p )because by default it will called as soon 
                # as an object is created
std1.__init__() # calling explicitly
# std1.message() # 0/p I'm a student (because here i'm calling)
print(dir(std1))  # no need to initialize, with the help of (dir) by default it will initialize

