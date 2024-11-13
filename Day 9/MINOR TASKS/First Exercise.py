student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

students_grades = {}

for students, score in student_scores.items():
    if score == 100:
        grade = 'Outstanding'
    elif score >= 91:
        grade = 'Outstanding'
    elif score >= 81:
        grade = 'Exceeds Expectations'
    elif score >= 71:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    students_grades[students] = grade

print (students_grades)
