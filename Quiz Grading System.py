# 1.4 Quiz Grading System
# A certain Computer Science professor gives 5-point quizzes that are graded on the following scale:
# Score Grade
# 5 A
# 4 B
# 3 C
# 2 D
# 1 F
# 0 F
# Write a program that accepts a quiz score (an integer between 0 and 5) as input and prints out the
# corresponding letter grade.

# <....program....>

marks = int(input())

if marks == 5:
    grade = 'A'
elif marks == 4:
    grade = 'B'
elif marks == 3:
    grade = 'C'
elif marks == 2:
    grade = 'D'
elif marks == 1:
    grade = 'E'
else:
    grade = 'F'
print(grade)