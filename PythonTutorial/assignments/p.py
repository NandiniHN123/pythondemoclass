# class StudentGradeTracker:
#     def __init__(self):
#         self.marks=[]
#         self.students_records=[]
#
#
#     def add_students(self,name,roll_no,m1,m2,m3):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks.append(m1)
#         self.marks.append(m2)
#         self.marks.append(m3)
#         print(f"NAME : {self.name}\nROLL_NO : {self.roll_no}\nMARKS : {self.marks}")
#
#
#
#     def average(self):
#         self.avg=sum(self.marks)/len(self.marks)
#         print("AVERAGE : ",self.avg)
#
# name=input("enter name") 
# roll_no=int(input("enter roll_no"))
# m1=int(input("enter m1="))  
# m2=int(input("enter m2="))
# m3=int(input("enter m3=")) 
# print() 
#
# s1=StudentGradeTracker()
# s1.add_students(name,roll_no,m1,m2,m3)
# s1.average()
'''
class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = []
            print(f"Student '{student_name}' added successfully.")
        else:
            print(f"Student '{student_name}' already exists.")

    def record_grade(self, student_name):
        if student_name in self.students:
            grades=[]
            for i in range(3):
                subject=input(f"enter marks for subject{i+1}:")
                grades.append(float(subject))
            return grades           
            if self.marks not in grades:
                self.marks.append(grades)
                self.students[student_name].append(grades)   
            try:
                if 0< subject >=100:
                    print(f"Grade recorded successfully for '{student_name}'.")
                else:
                    print("Invalid grade. Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for the grade.")
        else:
            print(f"Student '{student_name}' not found.")

    def calculate_average(self, student_name,):
        if student_name in self.students and len(self.students[student_name]) > 0:
            average = sum(grades) / len(grades)

    def display_report(self):
        print("\nStudent Grade Report:")
        for student, grades in self.students.items():
            average = sum(grades) / len(grades) 
            print(f"{student}: {grades} - Average: {average}")

# Example usage:
grade_tracker = StudentGradeTracker()

while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Record Grade")
    print("3. Calculate Average")
    print("4. Display Report")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        student_name = input("Enter student name: ")
        grade_tracker.add_student(student_name)

    elif choice == '2':
        student_name = input("Enter student name: ")
        grade_tracker.record_grade(student_name)

    elif choice == '3':
        student_name = input("Enter student name: ")       
        average = grade_tracker.calculate_average(student_name)
        print(average)

    elif choice == '4':
        grade_tracker.display_report()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
'''
class StudentGradeTracker:
    def _init_(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Student {name} added successfully.")
        else:
            print(f"Student {name} already exists.")

    def record_grade(self, name, subject, grade):
        try:
            grade = float(grade)
            if name in self.students:
                self.students[name].append((subject, grade))
                print(f"Grade recorded for {name} in {subject}.")
            else:
                print(f"Student {name} does not exist.")
        except ValueError:
            print("Invalid grade input. Please enter a numeric value.")

    def calculate_average(self, name):
        if name in self.students and len(self.students[name]) > 0:
            total_marks = sum(grade for subject, grade in self.students[name])
            average = total_marks / len(self.students[name])
            return average
        else:
            print(f"No grades recorded for {name}. Cannot calculate average.")

    def generate_report(self, name):
        if name in self.students:
            print(f"\nReport for {name}:")
            for subject, grade in self.students[name]:
                print(f"{subject}: {grade}")
            average = self.calculate_average(name)
            if average is not None:
                print(f"Average: {average}")
        else:
            print(f"Student {name} does not exist.")


tracker = StudentGradeTracker()

while True:
    print("\nOptions:")
    print("1. Add student")
    print("2. Record grade")
    print("3. Generate report")
    print("4. Quit")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        student_name = input("Enter student name: ")
        tracker.add_student(student_name)

    elif choice == '2':
        student_name = input("Enter student name: ")
        subject_name = input("Enter subject name: ")
        grade = input("Enter grade: ")
        tracker.record_grade(student_name, subject_name, grade)

    elif choice == '3':
        student_name = input("Enter student name: ")
        tracker.generate_report(student_name)

    elif choice == '4':
        print("Exiting the Student Grade Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")