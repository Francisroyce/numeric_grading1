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
    break

# age grade code / home work
def age_grades_chcild_teens_adults_centenarian (age) :
    if age <= 12:
        age_grade = 'Child'
    elif age <= 18:
        age_grade = 'Teen'
    elif age <= 99:
        age_grade = 'Adult'
    else:
        age_grade = 'centenarian'
    return age_grade
while True: #while loop with 'True boolean" has indefinite runtime
    age = float(input('Enter your age'))
    age_grade =age_grades_chcild_teens_adults_centenarian(age)
    print(age_grade)
    break

#'for' loops
text = 'hello world'
for c in text:
    print(c)

words = ['red', 'white', 'blue']
for word in words:
    print(len(word))

# the range function
for x in range(10) :
    print(x) # 0-9

#the break keyword ('for' loop)
for n in range (1, 100):
    for x in range (2, n): #if 1 is chosen, 1 will be printed throughout cos 1 is a factor of all the numbers
        if n % x == 0:
            print(n, 'has factor:', x)
            break
    else:
        print(n, 'is a  prime number')

for x in  range (10):
    if x % 2 != 0: # skip odds
        continue
    print(x)

beatles = ['francis', 'royce', 'blessing' 'anointed']
for i, member in enumerate(beatles):
    print('member (count) - (name)'.format (count=member, name=i))

for_else.py

for n in  [2, 4, 8, 22, 88, 1000]:
    if n % 2 != 0:
        print('odd number found', n)
        break
    else:
        print('no odd number found')



