#------- List Operations--------:

# 1 - Remove duplicates
'''
lst=[1,3,5,6,7,4,6,9,8]
n=[]
for i in lst:
    if i not in n:
        n.append(i)
        
print(lst)
print(n)
'''
#using dict function

'''
from _collections import OrderedDict
lst=[1,3,5,6,7,4,6,9,8]
n=list(OrderedDict.fromkeys(lst))
print(lst)
print(n)
'''
#using set
'''
lst=[1,3,5,6,7,4,6,9,8]
n=set(lst)
print(lst)
print(n)
'''

# 2 - create a function that returns the intersection(common elements) of two lists.
#using append function
'''
lst1=[1,2,3,4,5]
lst2=[3,4,5,2,7,9]
n=[]
def intersection():
    for i in lst1:
        if i in lst2:
            if i not in n:
                n.append(i)
    print(n) 
intersection()
'''
#without using append
'''
lst1=[1,2,3,4,5]
lst2=[3,4,5,2,7,9]
def intersection():
    for i in lst1:
        if i in lst2:
            print(i)
intersection()
'''

# 3 - list of squares of numbers from 1-10
'''
lst=[]
for i in range(1,11):
    lst.append(i)
    n=i**2
    print(n)
'''

#4 -  - Create a list of words that have more than 5 characters from a given list 
        # of words (you can create your own list of words for given list).
'''
lst1=["note","character","num","function"] 
lst2=[]
for i in lst1:
    if len(i)>5:
        lst2.append(i)
print(lst1)
print(lst2)
'''

'''
lst1=["note","character","num","function"]
lst2= []
for i in lst1:
    count = 0
    for j in i:
        count += 1  
    if count > 5:
        lst2.append(i)

print(lst1)
print(lst2)
'''

#------- Dictionary Operations --------:   

# Write a program to merge two dictionaries.
'''
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e',6:'f'}
d3=d1|d2
print(d3)
'''
# Create a function to find keys with duplicate values in a dictionary.

    
#------- Dictionary Iteration--------:      

#Write a program to iterate through keys and values of a dictionary and perform a specific operation on them.

    

#------- Tuple Operations--------:

# 1 - Reverse Tuple
"""
t=(1,2,3,4,5)
t=t[::-1]
print(t)
"""

#2 - Returns the common elements between two tuples

# t1=(1,2,3,4)
# t2=(5,4,2,6)
# def common(t1,t2):
#     for i in t1:
#         if i in t2:
#             return i
#     for j in t2:
#         if j in t1:
#             return j
#
# x=common()
# print(x)

#3 - Create a function to check if a certain key exists in a dictionary.


#------- Set Operations--------:

#union
'''
set1={1,2,3,4,5}
set2={6,5,4,9,8}
set3=set1|set2
print(set3)
'''     
#Intersection
#difference 
# set1={1,2,3,4,5}
# set2={4,3,2,7,6}
# for i in set1:
#     for j in set2:
#         if i not in set2 and j not in set1:
#             print(i,j)
        

                
          
# String operation using list

# def function(*n):
#     b=0
#     for i in n:
#         b=b+i
#     return b
# x=function(1,2,3,4)
#
# print(x)



