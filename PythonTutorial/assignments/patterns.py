#pattern 1:

# *
# * *
# * * *
# * * * *

for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()



#pattern 2:
'''
      *
    * *
  * * *
* * * *
'''



#pattern 3:
'''
* * * *
* * * 
* * 
* 
'''
'''
for i in range(4):
    for j in range(4-i):
        print("*", end=" ")
    print()
'''
'''
n=int(input("enter"))
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
'''
#pattern 4:
'''
* * * *
  * * *
    * *
      *
'''
# n= int(input("enter"))
# for i in range(n,0,1):
#     for j in range(n,i-1):
#         print("*", end=" ")
#     print()

