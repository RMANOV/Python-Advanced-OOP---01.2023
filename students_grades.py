# Students' Grades
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. 
# On the following N lines, you will be receiving a student's name and grade.
# For each student, print all his/her grades and finally his/her average grade, 
# formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

# Read the number of students
n = int(input())

# Create a dictionary to store the grades for each student
students = {}

# Read the names and grades for each student
for i in range(n):
    name, *grades = input().split()
    grades = [float(g) for g in grades]
    if name not in students:
        students[name] = []
    students[name] += grades

# Iterate over the students and calculate the average grade for each
for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} ->", end=" ")
    for grade in grades:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {average_grade:.2f})")
