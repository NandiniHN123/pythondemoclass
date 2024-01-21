#Assignment 1 - Print numbers from 1 to 10 using for loop
'''
for i in range(1,11):
    print(i)
'''

#Assignment 2 - Sum of numbers from 1-100 using for loop
'''
a=0
for i in range(1,101):
    a=a+i
print(a)
'''

#Assignment 3 - Multiplication Table (using for loop)
'''
m=int(input("enter a number"))
for i in range(1,11):
    mltpl=m*i
    print(m,'*',i,'=',mltpl)
'''

#Assignment 4 - Factorial of a number
'''
n=int(input("enter a number"))
a=1  
for i in range(1,n+1):
    a=a*i
print(a)
'''

#Assignment 5 -Sum of list
'''
lst=[]
x=int(input("enter how many numbers do you want to add"))
for i in range(x):
    n=int(input("enter elements"))
    lst.append(n)
    
c=0
for i in lst:
    c=c+i
print("sum :", c)
# print(sum(lst))                 #by using built-in function
'''

#Assignment 6 - Find maximum in list using for 
'''
lst=[]
x=int(input("enter a number"))
for i in range(x):
    n=int(input("enter list elements"))
    lst.append(n)
print(lst)
    
m=lst[0]    
for i in lst:
    if i>m:
        m=i
print("Maximum number is:", m)  
#print(max(lst))  
'''
# Find maximum in list using function
'''
lst=[2,5,6,4,3,8,1]
def m(x):
    n=x[0]
    for i in x:
        if i>n:
            n=i
    print("Maximum number is:", n)
 
m(lst) 
''' 

#Assignment 7 - count even numbers
'''
a=[]
even=0

x=int(input("enter a number"))
for i in range(x):
    n=int(input("enter elements"))
    a.append(n)
    
for i in a:
    if i%2==0:
        even=even+1
print("Total even numbers:", even)
'''

#Assignment 8 - Print Characters
'''
x=input("enter a string:")
for i in x:
    print(i)
print(type(x))
'''

#Assignment 9 - Print Prime numbers

# starting_no=int(input("enter the number where you want to start from"))
# end_number=int(input("enter the ending number"))
'''
for i in range(2,11):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
#Assignment 10 - Reverse a list
'''
lst=[]
x=int(input("enter a number")) 
for i in range(x):
    n=int(input("enter elements"))
    lst.append(n)
print(lst)
a=lst[::-1]
print(a)
'''

                
    
    
    
    