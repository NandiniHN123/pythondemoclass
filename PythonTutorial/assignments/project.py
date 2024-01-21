class StudentGradeTracker:
    def __init__(self):
        self.students=[]


    def add_students(self,name): 
        self.name=name
        self.students.append(name)
        
        
    def record_grade(self,name,marks):
        self.marks=[]
        if name in self.students:
            m1=int(input("enter m1="))  
            m2=int(input("enter m2="))
            m3=int(input("enter m3=")) 

            self.marks.append(m1)
            self.marks.append(m2)
            self.marks.append(m3)

            self.students[name].append(self.marks)

        else:    
            print(f"{name} not found")

    def calculate_average(self,name):
        average = sum(self.marks) / len(self.marks)
        print(average)

    # def details(self):
    #     print(f"{name} {marks} {average} {students}")    
tracker=StudentGradeTracker()
    i=1
    choice=(1,2,3,4,5)
    x=int(input("enter your choice from 1-5"))
    for i in choice:
        if x ==i:
            name=input("enter name:")
            tracker.add_students(name)
        elif x==i:
            name=input("enter name:")
            marks=int(input("enter marks:"))
            tracker.record_grade(name,marks)
        elif x==i:
            name=name=input("enter name:")
            marks=int(input("enter marks:"))
            tracker.calculate_average(name,marks)
            
main()
# name=input("enter name") 

# s1=StudentGradeTracker()
# s1.add_students(name)
# s1.record_grade()
# s1.calculate_average()
# s1.details()


        
        
        
        
        