# Student Credits
# Diyan is a student and he wants your help.
# He wants a program that calculates whether he gets a diploma or not.
# Write a function students_credits which receives a different number of strings.
# Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
# Your task is to calculate the credits Diyan manages to get from all courses.
# The credits he gets are proportional to his points on the test.
# For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test points,
# he will get 12.5 credits for the course.
# Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's credits.
# Finally, return a string on multiple lines containing:
# •	Diyan's achievement message:
# o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
# o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
# •	Information for each course and Diyan's credits:
# o	"{course name} - {diyan's credits}"
# o	Note: Each course data should be on a new line.
# •	All credits must be formatted to the first decimal place.

# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just any number of strings with courses data passed to your function
# Output
# •	The function should return a string in the format described above:
# Constraints:
# •	There will always be at least one course.
# •	There will not be two or more courses with the same name.
# •	All points and all credits will be whole numbers


def students_credits(*args):
    courses = {}
    final_print = []
    for arg in args:
        course, credits, max_points, diyan_points = arg.split("-")
        courses[course] = [int(credits), int(max_points), int(diyan_points)]

    for course, data in courses.items():
        credits, max_points, diyan_points = data
        courses[course] = credits * (diyan_points / max_points)

    sorted_courses = dict(sorted(courses.items(), key=lambda x: x[1], reverse=True))
    total_credits = sum(sorted_courses.values())

    if total_credits >= 240:
        print(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        print(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for course, credits in sorted_courses.items():
        final_print.append(f"{course} - {credits:.1f}")
    
    return "\n".join(final_print)


students_credits("Computer Science-12-300-250", "Basic Algebra-15-400-200", "Algorithms-25-500-490")
