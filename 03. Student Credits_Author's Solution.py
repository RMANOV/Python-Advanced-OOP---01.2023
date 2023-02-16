def students_credits(*args):
    diyan_total_credits = 0
    diyan_credits_info = dict()
    final_strings = []

    for info in args:
        course_name, course_credits, max_test_points, dian_points = info.split("-")
        current_percentage = int(dian_points) / int(max_test_points)
        diyan_current_credits = current_percentage * int(course_credits)
        diyan_total_credits += diyan_current_credits
        diyan_credits_info[course_name] = diyan_current_credits

    if diyan_total_credits >= 240:
        final_strings.append(
            f"Diyan gets a diploma with {diyan_total_credits:.1f} credits."
        )
    else:
        final_strings.append(
            f"Diyan needs {240-diyan_total_credits:.1f} credits more for a diploma."
        )
    sorted_dian_points_info = sorted(diyan_credits_info.items(), key=lambda a: -a[1])

    for course, points in sorted_dian_points_info:
        final_strings.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_strings)
