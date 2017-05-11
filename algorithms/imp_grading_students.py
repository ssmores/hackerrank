"""HackerRank Algorithm Problems.

Grading Students

HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process. For each grade(i), round it according to the rules above and print the result on a new line.


Input Format

The first line contains a single integer denoting n (the number of students). 
Each line i of the n subsequent lines contains a single integer, grade(i), denoting student i's grade.

Constraints
1 <= n <= 60
0 <= grade(i) <= 100

Output Format

For each grade(i) of the n grades, print the rounded grade on a new line.

Sample Input 0

4
73
67
38
33


Sample Output 0

75
67
40
33


Explanation 0

    ID  Original grade  Final grade
    1   73              75
    2   67              67
    3   38              40
    4   33              33

Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.

Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70 - 67 = 3, the grade will not be modified and the student's final grade is 67.
Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40 - 38 < 3, the student's grade will be rounded to 40.
Student 4 received a grade below 38, so the grade will not be modified and the student's final grade is 33.



**************
Featured solutions 
Python 2

Observation
The difference between the student's grade and the next multiple of 5 will be less than 3 if grade mod 5 >= 3. For example, let's consider values for grade in the inclusive interval from 80 through 54:
80 mod 5 = 0 because 5 evenly divides 80, so this would remain unchanged.
81 mod 5 = 1, so this would remain unchanged.
82 mod 5 = 2, so this would remain unchanged.
83 mod 5 = 3, so this would be rounded up to the next multiple of 5.
84 mod 5 = 4, so this would be rounded up to the next multiple of 5.
85 mod 5 = 5, so this would remain unchanged.
If you perform the same calculations for the grade interval from 85 through 90, you'll see the same results.

Solution
As long as grade >= 38, using grade mod 5 >= 3 allows us to determine when we need to round a grade. We can then either:
1. Use a while loop to increment grade to the next multiple of 5.
Python 2
n = int(raw_input().strip())

for a0 in xrange(n):
    grade = int(raw_input().strip())

    if grade>=38 and grade%5>=3:
        while grade%5!=0:
            grade = grade + 1
    print grade


2. Add the result of 5 - (grade mod 5) to grade.
Python 2
n = int(raw_input().strip())

for a0 in xrange(n):
    grade = int(raw_input().strip())

    if grade >= 38 and grade % 5 >= 3:
        grade = grade + 5 - (grade % 5)
        
    print grades

**************
"""

#!/bin/python

import sys

def solve(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade) 
        else:
            l_num = str(grade)[1]

            if l_num == '8' or l_num == '3':
                new_grades.append(grade + 2)

            elif l_num == '9' or l_num == '4':
                new_grades.append(grade + 1)
            else:
                new_grades.append(grade)
            
    return new_grades



# This was provided and could be modified.
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))