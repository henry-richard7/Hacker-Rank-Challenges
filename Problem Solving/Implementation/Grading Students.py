def get_nearest_5(n):
    if n % 5 != 0:
        n = n + (5 - n % 5)
        return int(n)
    else:
        return n


def gradingStudents(grades):
    result_grades = []
    for grade in grades:
        nearest_difference = abs(grade - get_nearest_5(grade))
        if grade > 37:
            if nearest_difference < 3:
                result_grades.append(grade + nearest_difference)
            else:
                result_grades.append(grade)
        else:
            result_grades.append(grade)
    return result_grades


grades = []
grades_count = int(input().strip())
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print('\n'.join(map(str, result)))
