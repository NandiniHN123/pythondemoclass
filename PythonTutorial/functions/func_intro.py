'''
Function: set of code which performs a particular task
Built-in function: print, input, id, type etc.,,,
User defined functions 

advantages: 
1. Increases code re-usability
2. Code maintenance is easier
'''
'''
def welcome():   # function without arguments
    print("Welcome to python program")
    
welcome() 
'''   

def add(a,b):    # function with arguments
    c=a+b
    print(c)

add(2,3)
add(4,2)
add(5,3)


'''
def add(a,b):
    c=a+b
    #print c
    return c
x=add(2,3)    #extra variable to store return value
y=x**2
print(x)
print(y)
'''

def add_mul(a,b):
    c=a+b    # calling add function
    d=a*b
    print(c,d)
    return c,d 
x,y=add_mul(5,8) 
print(x)
print(y)
