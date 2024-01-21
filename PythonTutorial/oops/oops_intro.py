'''
- class
- types of variables (class , method and object)
- constructor

different between variable and object in Python
when 2 variables have same values, it is store at the same location
but when we create two object from the same class that is stored at different location 

'''
'''
class CarClass:
  
    def move_forward(self,name):   # method (function inside a class)  #we are not passing value to self - by default it takes object as value
        print(f"{name} Car is moving forward")  # f- formating or formalizing the string- use {} as place holders for a variables
    
    def move_backward(self,name):
        print(f"{name} Car is moving backward")  
         
swift=CarClass()
duster=CarClass()
print(type(swift))
print(type(duster))
print(id(swift))
print(id(duster)) 
                  
# move-forword()  # I can't call the function directly which is inside the class
swift.move_forward("swift") # with the help of object I can access the method inside class
duster.move_forward("duster")
swift.move_backward("swift")
'''
'''
#constructor

class CarClass:

    def __init__(self,name): # instead  of declaring name in every function we can declare it here once.
        self.name=name       # to covert local variable name into method variable
# self.name = by default object parameter pass to the self (i.e swift, duster), and we are passing name parameter to name 
#self parameter takes object as value(swift), we give values only to name.
    def move_forward(self):    # no need to declare name here    
        print(f"{self.name} Car is moving forward")  # use self.name variable instead of name variable
    
    def move_backward(self):
        print(f"{self.name} Car is moving backward") 
        
swift=CarClass("swift")  #here i need to pass that value
duster=CarClass("duster")

swift.move_forward()  #after initiate name as method, no need to pass values here
duster.move_backward()

print(swift.name)
print(duster.name)
'''
# types of Variables

class CarClass:
    
    company="abc"  #class variable (it is unchanged) 
    
    def __init__(self,name):
        self.name=name
        
    def display_details(self):
        print(f"{self.name} Car is created for {CarClass.company} company ")
  
    def move_forward(self):         #Method Variable
        print(f"{self.name} Car is moving forward")   #Instance/Object Variable

    def move_backward(self,speed):         #Method Variable
        print(f"{self.name} Car is moving backward at {speed} kmph ")
        
swift=CarClass("swift")
duster=CarClass("duster")

swift.move_forward()  
duster.move_forward()      
swift.display_details()        #i'm not passing any company name for both but it same for both.
duster.display_details()
swift.move_backward(50)# here i need to give value because i didn't initialize it , this is a method variable
duster.move_backward(100)
