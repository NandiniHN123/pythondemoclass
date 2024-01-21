"""
conditional statements
1. If statement
2. If-else statement
3. If elif statement (series if-else statement)
4. nested If-else statements
"""

'''

age=int(input("please enter your age:"))
'''
'''
if age>13:
    print("Age is satisfied")
else:
    print("Age is not satisfied")
print("program is terminated")
'''
age=int(input("please enter your age:"))
if age >18:
    print("you're an adult")
elif age >=13:
    print("you're a teenager")
else:
    print("you are a child")

"""  
if age>=13:
    if age>18:
        print("you're an adult")
    else:
        print("you're a teenager")
else:
    print("you're a child")'''
"""    
"""
x=int(input("enter a number"))
if x%2==0:
    print("even")   
else:
    print("odd")
"""  