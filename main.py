#If statement (mumeric_grading)
def numeric_grade_to_letter_grade(numeric_grade) :
    if numeric_grade >= 90:
        letter_grade = 'A'
    elif numeric_grade >= 80:
        letter_grade = 'B'
    elif numeric_grade >= 70:
        letter_grade = 'C'
    elif numeric_grade >= 60:
        letter_grade ='E'
    else:
        letter_grade = 'F'
    return letter_grade
while True:
    numeric_grade = float(input('Enter grade percentage'))
    letter_grade = numeric_grade_to_letter_grade(numeric_grade)
    print(letter_grade)
