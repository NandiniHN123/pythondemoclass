'''
Tuple():
1.Empty tuple can be created
2.Tuple is heterogeneous
3.Tuple can't be modified
4.Tuple can be created with duplicate element
'''
a=()  # empty tuple
#print(a)
#print(type(a))

b=(1,2,3,4,5,5,6,7,8,9,10)   # tuple with elements
print(b)
# print(type(b))

c=tuple(range(1,5))   #creating tuple using built-in function
#print(c)
#print(type(c))

d=(3, "xyz", 2.3, 2+6j, True)  # different data types
#print(d)
#print(type(d)) 

# b=(1,2,3,4,5,6,7,8,9,10)     #accessing individual element using indexing
# print(b)
#print(b[3])

#for i in b:
#    print(i)
#print(b[3])

d=(3, "xyz", 2.3, 2+6j, True) #we can't change 
#d[2]="abc"
#print(d)

#print(b[0:5])
#print(b[4:9])
#print(b[4:])
#print(b[:3])
#print(b[::3])
# print(b[-11:-5:2])
# print(b[-2:-9:-1])
# print(b[::-1])

print(b.count(d))
print(d)




print(b.index(6, 2, 9))

    