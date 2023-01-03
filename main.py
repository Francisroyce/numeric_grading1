# # If statement (mumeric_grading)
# def numeric_grade_to_letter_grade(numeric_grade):
#     if numeric_grade >= 90:
#         letter_grade = 'A'
#     elif numeric_grade >= 80:
#         letter_grade = 'B'
#     elif numeric_grade >= 70:
#         letter_grade = 'C'
#     elif numeric_grade >= 60:
#         letter_grade ='E'
#     else:
#         letter_grade = 'F'
#     return letter_grade
# while True:
#     numeric_grade = float(input('Enter grade percentage'))
#     letter_grade = numeric_grade_to_letter_grade(numeric_grade)
#     print(letter_grade)
#     break
#
# # age grade code / home work
# def age_grades_chcild_teens_adults_centenarian (age) :
#     if age <= 12:
#         age_grade = 'Child'
#     elif age <= 18:
#         age_grade = 'Teen'
#     elif age <= 99:
#         age_grade = 'Adult'
#     else:
#         age_grade = 'centenarian'
#     return age_grade
# while True: #while loop with 'True boolean" has indefinite runtime
#     age = float(input('Enter your age'))
#     age_grade =age_grades_chcild_teens_adults_centenarian(age)
#     print(age_grade)
#     break
#
# #'for' loops
# text = 'hello world'
# for c in text:
#     print(c)
#
# words = ['red', 'white', 'blue']
# for word in words:
#     print(len(word))
#
# # the range function
# for x in range(10) :
#     print(x) # 0-9
#
# #the break keyword ('for' loop)
# for n in range (1, 100):
#     for x in range (2, n): # if 1 is chosen, 1 will be printed throughout cos 1 is a factor of all the numbers
#         if n % x == 0:
#             print(n, 'has factor:', x)
#             break
#     else:
#         print(n, 'is a  prime number')
#
# for x in  range (10):
#     if x % 2 != 0: # skip odds
#         continue
#     print(x)
#
# beatles = ['francis', 'royce', 'blessing' 'anointed']
# for i, member in enumerate(beatles):
#     print('member (count) - (name)'.format (count=member, name=i))
#
# # for_else.py
#
# for n in  [2, 4, 8, 22, 88, 1000]:
#     if n % 2 != 0:
#         print('odd number found', n)
#         break
#     else:
#         print('no odd number found')
#
# # execute
# # exec function
# exec('print("hello world")')
#
# for n in (0, 1, 2, 3, 4, 5,):
#     print(n*n)
#
# exec('for n in (0, 1, 2, 3, 4, 5): print(n*n)')
#
# # iterable object
# print('one')
# list = [1, 2,3]
# iterable = iter(list)
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
#
# print('two')
# iterable = iter(list)
# for items in iterable:
#     print(items)
#
# print('three')
# for items in list:
#     print(items)
#
# # exception
# # zeroDivisonOnError
# while True:
#     try:
#          x = int (input('Please enter a number:\n'))
#          break
#     except ValueError:
#         print('oops! that was no valid number.  Try again...')
# # # try statement may have more than one except clause
# import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int (s.strip())
# except IOError as err:
#     print('I/O error: {0}'.format(err))
# except ValueError:
#     print('could not convert data to an integer.')
# except:
#     print('unexpected error:', sys.exc_info()[0])
#     raise
#
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readline()), 'lines')
#         f.close()
# # Data types
# print(type(1))
# print(type(1.0))
# import fractions
# print(type(fractions.Fraction(1, 2)))
# print(type(1/2))
# print(type(1j))
# print(type('cool'))
# print(type(True))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(set([])))
# print(type(fractions))
# print(type(int(3.14)))
# print(type(None))
# print(isinstance(1, int))
# print(isinstance(1.0, int))
# print(isinstance(1, float))   #etc
# import fractions
# # numbers
# import math
# print(math.pi)
# print(2*3)
# print(2**3)
# print(math.sqrt(10))
# print(math.floor(math.pi))
# print(math.ceil(math.pi))
# print(math.exp(1))
# print(math.log(math.e))
# print(math.log10(100))
# print(math.pow(10, 3))
# print(math.sin(math.pi/6))
# print(math.cos(math.radians(60)))
#
# print(0x2A)
# print(int('42'))
# print(float(42), int(2.6))
# print(0x0 << 3)
#
# fraction1 = fractions.Fraction(1, 2)
# fraction2 = fractions.Fraction(11, 20)
# fraction3 = fraction1 + fraction2
# print(fraction3)
# print(float(fraction3))
# print(1j * (3 + 4j))
# print(1j * 3 + 4j)
#
# import random
# print(random.random())
# print(random.random)
# print(0x0000025B38DA5D30)
#
# import random
# print(random.randint(1, 1000))
#
# import decimal
# decimal1 = decimal.Decimal('3.14')
# print(decimal1)
#
# print(True + False)
# # print(1/0) #undefined
#
# # numerical operations next
# fractions
import fractions
x = fractions.Fraction (16, -10)
print(x)
print(float(x))
print(2*x)

x = fractions.Fraction(2.25)
print(x)
print(int(x))
print(float(x))

a = 42
b = 56
x = fractions.Fraction(a, b)
print(x)

# a = 42
# b = 56
# x = fractions.Fraction(a, b)
# print(x)
# gcd = fractions.gcd(a, b)
# print('gcd of 42 and 56:', gcd)

x = fractions.Fraction(3, 5)
y = fractions.Fraction(7, 11)
z = x*y
print(z)
print(float(z))

# arithmetic operations
result = 1 + 2 * 3/4
print(result)

result = 1 + (2* 3)/ 4
print(result)

result = 1 + 2* (3/4)
print(result)

result = (1 + 2) * 3/4
print(result)

# modulo operator
remainder = 10 % 3
print(remainder)

# power operator
print(3**2)
a = 3
b = 2
print(a**b)

# division operators
print(10 / 3)
print(int(10/3))
print(10.0/3)
print(10//3)

# bitwise
a = 0b00111100
b = 0b00001101
print(a)
print(b)

# swap
x =1
y = 2
print(x, y)
x = y
y = x
print(x, y)

x = 1
y =2
print(x,y)
temp = x
x = y
y = temp
print(x, y)

x = 1
y = 2
x, y = y, x
print(x, y)

