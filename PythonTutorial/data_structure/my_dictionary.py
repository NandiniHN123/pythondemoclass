'''
in dictionary elements will be stored in the form of key-value pair

'''
a=[1,2,3,4,5]
d={1:"indresh", 2:"leander", 3:"nandini", 4:"soundarya"}
print(d)
print(d[3])
d[1]="indresh Indu"
print(d)
c=d.fromkeys(a, None)
print(c)
print(d.keys())
print(d.values())