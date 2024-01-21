'''
Function arguments:

category 1: Formal Arguments
a. default arguments
b. Variable-Length arguments
c. keyword variable-Length arguments

category 2: Actual arguments
a. Positional arguments
b.  Key word arguments


'''
#from functions.func_intro import add_mul
'''
def add(a=0,b=0): #Formal arguments, (a=0,b=0)default arguments
    c=a+b
    print(c)
'''  
'''
add(2,4)   # Actual arguments, positional arguments(based on position values will be assigned
add(b=4,a=3) #keyword arguments
add(1) 
'''
'''
def display(*a):  #variable length arguments
    print(a)
'''
'''
display(1,2)       # veriable length arguments accepts only values
#display(a=1,b=2)   #error(we can't pass keys
'''
'''
def save(**a): #keyword variable length arguments
    print(a)
save(name="abc", roll_no=1)
save(2) #error(it can't pass positional arguments)
'''
'''
def save(*b, **a): #keyword variable length arguments
    print(b)
    print(a)
    
save(1,name="abc", roll_no=1)
'''
'''
add_mul(1,4)   #import add_mul function from other module
'''


#assignment :add all the tuple elements
'''
def adition(*n):         #n=(c=0,1,2,3,4,5,6,7,8,9,10)
    c=0
    for i in n:
        c=c+i
        #print(c)        #o/p 10 30 60 100
    print(c)             #o/p 100
    
    
adition(10,20,30,40)    
'''


    