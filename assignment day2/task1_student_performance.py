
# Smart Student Performance Checker

# 1. Input student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# 2. Input marks for 5 subjects
subjects = {
    "Math": float(input("Enter Math marks: ")),
    "Science": float(input("Enter Science marks: ")),
    "English": float(input("Enter English marks: ")),
    "Social Science": float(input("Enter Social Science marks: ")),
    "Computer": float(input("Enter Computer marks: "))
}

# 3. Calculate total and percentage
total = sum(subjects.values())
percentage = (total / 500) * 100

# 4. Find highest and lowest subject scores
highest_subject = max(subjects, key=subjects.get)
lowest_subject = min(subjects, key=subjects.get)

highest_marks = subjects[highest_subject]
lowest_marks = subjects[lowest_subject]

# 5. Check PASS or FAIL
if all(marks >= 35 for marks in subjects.values()):
    result = "PASS"

    # 6. Assign grade only if the student passes
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    # 7. Performance message
    if grade in ("A+", "A"):
        message = "Excellent Performance"
    elif grade == "B":
        message = "Good Performance"
    else:
        message = "Needs Improvement"

else:
    result = "FAIL"
    grade = "N/A"
    message = "Failed. Try Again"

# 8. Consistency check
if highest_marks - lowest_marks > 40:
    consistency = "INCONSISTENT PERFORMANCE"
else:
    consistency = "Consistent Performance"

# 9. Display student report
print("\n========== STUDENT REPORT ==========")
print("Student Name:", student_name)
print("Roll Number:", roll_number)

print("\nSubject-wise Marks:")
for subject, marks in subjects.items():
    print(f"{subject}: {marks:g}/100")

print("------------------------------------")
print(f"Total Marks: {total:g}/500")
print(f"Percentage: {percentage:.2f}%")
print("Result:", result)
print("Grade:", grade)
print("Performance:", message)

print("\nHighest Score:", highest_subject, "-", f"{highest_marks:g}")
print("Lowest Score:", lowest_subject, "-", f"{lowest_marks:g}")
print("Consistency:", consistency)
print("====================================")
