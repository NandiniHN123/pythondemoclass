# Functions:

# 1- Create a function that takes two numbers as arguments and returns their sum.
'''
a = 5
b = 7
def add(a,b):
    return a+b


result = add(a,b)
print(f"The sum of {a} and {b} is: {result}")
'''

# 2 - Write a function that takes a string and an optional parameter to specify the number of
    # times the string should be repeated (default should be 1).
    
    
# 3 - Implement a function that takes a variable number of arguments and returns their sum.   
'''
def addition(*n):         #n=(i=10,20,30,40)
    c=0
    for i in n:
        c=c+i
    return c
 
x=addition(10,20,30,40)   
print(x)
'''

# 4 -  Write a recursive function to calculate the factorial of a given number.
'''
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)

number = 5
result = facto(number)

print(f"factorial of {number} is: {result}")
'''

# 5 - Create a recursive function to generate the Fibonacci sequence up to a specified limit.
'''
def fibonacci(limit, a=0, b=1, sequence=[]):
    if a > limit:
        return sequence
    else:
        sequence.append(a)
        return fibonacci(limit, b, a + b, sequence)
    
limit = 50
fibonacci = fibonacci(limit)

print(f"Fibonacci sequence up to {limit}: {fibonacci}")
'''

# 6 -   Write a function that takes another function as an argument and applies it to a list of numbers.
'''
def a(func, numbers):
    result = [func(num) for num in numbers]
    return result


def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

result = a(square, numbers)

print(f"Original list: {numbers}")
print(f"Applying square function: {result}")
'''