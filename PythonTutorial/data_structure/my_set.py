'''
Set{}:
1. Empty set can't be created
2. Set is heterogeneous - list can be created with diff data type elements
3. Set can't be modified
4. Set can't be created with duplicate element
'''
# a={}       # Empty set can't be created
# print(a)
# print(type(a))  # <class 'dict'>

b={1,2,3,4,5,6,7,8,9,10}         # set with elements
print(b)
#print(type(b))

#c=set(range(1,10))         #creating set using built-in function
#print(c)
#print(type(c))

#d={3, "xyz", 2.3, 2+6j, True}    # different data types
#print(d)
#print(type(d))

# b={1,2,3,4,5,6,7,8,9,10}     #can't accessing individual element using index no.
# print(b)
# print(b[3])

# for i in b:
#    print(i)
#     print(b[3])
#

d={3, "xyz", 2.3, 2+6j, True} #we can't modify
d[2]="abc"
print(d)

b={1,2,3,4,5,5,6,7,8,9,10}         # can't be created with duplicate element
print(b)
