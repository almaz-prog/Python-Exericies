# // 1.5 Exam Grading System
# // A certain Computer Science professor gives 100-point exams that are graded on the following scale:
# // Score Range     Grade
# // 90 – 100         A
# // 80 – 89          B
# // 70 – 79          C
# // 60 – 69          D
# // Below 60         F
# // Write a program that accepts an exam score as input and prints out the corresponding letter grade.
# // Input Format
# // A single integer score (0 ≤ score ≤ 100) representing the exam score.
# // Output Format
# // Print a single line containing the corresponding letter grade (A, B, C, D, or F)

# // Program:

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