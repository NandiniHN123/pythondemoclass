#Assignment 1 - Even or odd 
'''
x=int(input("enter a number:"))
if x%2 == 0:
    print("Even number")
else:
    print("odd number") 
 '''   
 
#Assignment 2 - Grade calculator (using logical operators)

'''
score=int(input("enter a score:"))
if score>=90 and score<=100:
    print("A")
elif score>=80 and score<=89:
    print("B")
elif score>=70 and score<=79:
    print("C")
elif score>=60 and score<=69:
    print("D")
elif score<60:
    print("F")  
else:
    print("Invalid score")   
'''

#Assignment 3 - Age group(using logical operators)
'''
age=int(input("enter your age:"))
if age<=12:
    print("you're a child")
elif age<=17:
    print("you're a Teenager")
elif age<=64:
    print("you're an adult")
else:
    print("you're a senior citizen")  
'''

#Assignment 4 - Leap year or NOt - a leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400

#method 1
'''
year=int(input("enter a year"))
if year%4==0:
    if year%100!=0:
            print(year,"is a leap year")
    elif year%400==0:
            print(year, "is a leap year")
else:
    print(year,"is not a leap year")
        
'''       
#method 2  
'''
year=int(input("enter a year"))
if year%4==0 and year%100!=0 or year%400==0:  
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")   
'''

#Assignment 5 - Positive or Negative (a>0=+, a<0=-)
'''
a=int(input("enter a number"))
if a>0:
    print("Positive number")
elif a<0:
    print("Negative number")   
else:
    print("zero")
'''

#Assignment 6 - Vowel or Consonant
'''
x=input("enter a character:")
vowel=('a','e','i','o','u','A','E','I','O','U')
if x in vowel:
    print("vowel")
else:
    print("consonant")
'''

#Assignment 7 - Maximum of 3 numbers
'''
def h(a,b,c):
    if a>b and a>c:
        print("max is a=",a)
    elif b>a and b>c:
        print("max is b=",b)
    else:
        print("max is c=",c)
h(6,3,9)
'''
    
#Assignment 8 - Triangle type (Equilateral(3sides equal), Isosceles(any 2sides equal), Scalene(diff))
'''
def triangle(a,b,c):
    if a==b and b==c and c==a:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")
        
triangle(4,4,4)
'''
    
#Assignment 9 - Login system
'''
name=input("please enter a valid User name:")
pw=input("please enter a valid password:")
if name=='admin' and pw=='password123':
    print("login successful")
else:
    print("Login failed")
'''    

#Assignment 10 - Divisibility check (divisible by 3 and 5 or not)
'''
def check(a):
#a=int(input("enter a number"))
    if a%3==0 and a%5==0:
        print(a,"is Divisible by both")
    else:
        print(a,"is Not Divisible by both")
        
check(30)
'''

#Assignment - add all the tuple elements

#  by taking range from user
'''
strt=int(input("enter"))
end=int(input("enter"))
c=0
for i in range(strt, end+1):
    c=c+i
print(c)
'''
# by creating function 
'''
def addition(*n):         #n=(i=10,20,30,40)
#n=(10,20,30,40)
    c=0
    for i in n:
        c=c+i
        #print(c)        #o/p 10 30 60 100  
    # print(c)             # o/p 100
 
addition(10,20,30,40)    
'''

    
