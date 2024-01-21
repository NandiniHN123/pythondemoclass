'''
Exception: which is not normal/ abnormal

Errors:
1. Syntax errors: these are completely under programmer's control
2. Run-time errors: unexpected
'''
print(2+3)
print(2*3)
try:
    try:
        print(10/"abc")
    
# except:                   # default except block
#     print("there is an error") 

# except ZeroDivisionError as Ze:       # individual except block
#     # print("there is a zero division error")
#     print("Error msg:", Ze)
#
# except TypeError as Te:               # individual except block
#     # print("there is a type error")
#     print("Error msg:", Te)
  
    
    except (ZeroDivisionError, TypeError) as k:      #Handling multiple exception in 1 line
        print("Error msg:", k)
        print(10/0)

except Exception as e:               #if there is an error in except block
    print("Error msg:", e)
print(5%2)
print(22//2)
