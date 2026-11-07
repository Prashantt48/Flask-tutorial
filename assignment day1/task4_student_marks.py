students = {}

number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):
    name = input(f"Enter name of student {i + 1}: ")
    marks = float(input(f"Enter marks for {name}: "))

    students[name] = marks

if students:
    highest_student = max(students, key=students.get)

    print("\nStudent Marks:", students)
    print("Student with highest marks:", highest_student)
    print("Highest marks:", students[highest_student])
else:
    print("No student records entered.")