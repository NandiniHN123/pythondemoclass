class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = []
            print(f"Student '{student_name}' added successfully.")
        else:
            print(f"Student '{student_name}' already exists.")

    def record_grade(self, student_name, grade):
        if student_name in self.students:
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    self.students[student_name].append(grade)
                    print(f"Grade recorded successfully for '{student_name}'.")
                else:
                    print("Invalid grade. Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for the grade.")
        else:
            print(f"Student '{student_name}' not found.")

    def calculate_average(self, student_name):
        if student_name in self.students:
            grades = self.students[student_name]
            if grades:
                average = sum(grades) / len(grades)
                return f"The average grade for '{student_name}' is: {average}"
            else:
                return f"No grades recorded for '{student_name}'."
        else:
            return f"Student '{student_name}' not found."

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
        grade = input("Enter grade: ")
        grade_tracker.record_grade(student_name, grade)

    elif choice == '3':
        student_name = input("Enter student name: ")
        result = grade_tracker.calculate_average(student_name)
        print(result)

    elif choice == '4':
        grade_tracker.display_report()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")