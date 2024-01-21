'''
#1. Constructor, inheritance, polymorphism
#2. abstraction
'''
#1. Constructor, inheritance, polymorphism
'''
class TataProperty:
    
    def __init__(self, name, age):
        print(f"{name} Tata's property age of {age}")
    
class AppaPrroperty(TataProperty):   
    def __init__(self, name, age):
        print(f"{name} Appa's property age of {age} ")
        
    def car(self):
        print("this is appa's car")
     
class AmmaProperty:   
    def Amma(self):
        print("Amma's property")
        
    def car(self):
        print("this is amma's car")
        
class ChildProperty(AppaPrroperty,AmmaProperty):
    def child(self):
        print("child's property") 
            
obj1=TataProperty("subbu", 89)
# obj1.tata()
print()

obj2=AppaPrroperty("nataraju", 67)
# obj2.appa()
# obj2.tata()
# obj2.car()
print()

# obj3=AmmaProperty()
# obj3.Amma()
# obj3.car()
print()

obj4=ChildProperty("nandu", 22)
# obj4.child()
# obj4.appa()
# obj4.tata()
# obj4.Amma()
# obj4.car()
print(ChildProperty.mro())
print()
'''

#2. abstraction
'''
from abc import ABC, abstractmethod
 
class Textbook(ABC):
    def pages(self):
        print("500 pages")
    @abstractmethod 
    def form(self):
        pass
    
class Notebook(Textbook):
    
    def form(self):
        print("king size")
    def show(self):
        print("this is notebook")

   
hn=Notebook()
hn.show()
hn.form()
hn.pages()
'''

#Encapsulation:
'''
class CarClass:
    company="hn"
    
    def __init__(self, name, roll_no):
        self._name=int(input("enter"))
        self.__roll_no=roll_no
        
        
    def move_frwrd(self, speed):
        self.speed=speed
        print(f"is moving frwrd at {self.speed} kmph")
        
car1=CarClass("abc", 345)
print(car1._name)
try:
    print(car1.move_frwrd(22))
except:
    print("wrong")
print(CarClass.mro())    
'''
class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def record_grade(self, name):
        if name in self.students:
            grades=[]
            for i in range(3):
                subject=input(f"enter marks for subject{i+1}:")
                grades.append(float(subject))   
            self.students[name].append(grades)
            print(f"{self.students} ")
        else:
            print(f"Student '{name}' not found.")

    def calculate_average(self, name):
        if name in self.students: 
            average = sum(self.students[name]) / len(self.students[name])
            return average
        else:
            return None

    def display_report(self):
        print("\nStudent Grade Report:")
        for name, grades in self.students.items():
            average = self.calculate_average(name)
            if average is not None:
                print(f"{name}: Grades {grades}, Average: {average:.2f}")
            else:
                print(f"{name}: No grades recorded.")


tracker = StudentGradeTracker()

while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Record Grade")
    print("3. Calculate Average")
    print("4. Display Report")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        tracker.add_student(name)
    elif choice == "2":
        name = input("Enter student name: ")
        tracker.record_grade(name)
    elif choice == "3":
        name = input("Enter student name: ")
        average = tracker.calculate_average(name)
        if average is not None:
            print(f"Average for {name}: {average}")
        else:
            print(f"No grades recorded for {name}.")
    elif choice == "4":
        tracker.display_report()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



   
    
    
    
     
