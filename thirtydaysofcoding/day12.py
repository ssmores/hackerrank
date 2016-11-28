"""30 days of coding for HackerRank.


Day 12: Inheritance
by AllisonP

Objective
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

    A Student class constructor, which has 4 parameters:
        A string, firstName.
        A string, lastName.
        An integer, id.
        An integer array (or vector) of test scores, scores.
    A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

    Grading Scale
    Letter  Average(a)
    O       90 <= a <= 100
    E       80 <= a < 90
    A       70 <= a < 80
    P       55 <= a < 70
    D       40 <= a < 55
    T       a < 40

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains firstName, lastName, and id, respectively. The second line contains the number of test scores. The third line of space-separated integers describes scores.

Constraints
4 <= |firstName|, |lastName| <= 10
|id| === 7
0 <= score, average <= 100

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80

Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O


Explanation

This student had 2 scores to average: 100 and 80. The student's average grade is (100 + 80)/2 = 90. An average grade of 90 corresponds to the letter grade O, so our calculate() method should return the character'O'.



**************
Featured solutions 
Python 2 or 3
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = scores
        
    def calculate(self):
        average = 0
        for i in self.testScores:
            average += i

        average = average / len(self.testScores)
        
        if(average >= 90):
            return 'O' # Outstanding
        elif(average >= 80):
            return 'E' # Exceeds Expectations
        elif(average >= 70):
            return 'A' # Acceptable
        elif(average >= 55):
            return 'P' # Poor
        elif(average >= 40):
            return 'D' # Dreadful
        else:
            return 'T' # Troll



**************
"""

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

# This is the class that needs to be filled out.
class Student(Person):
    """Contains an array of integers for test scores."""
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        """Calculates student's average score and returns letter grade."""

        s_sum = 0
        class_num = len(self.scores)
        
        for i in range(class_num):
            s_sum += self.scores[i]

        av = float(s_sum)/class_num
        if av >= 90:
            return 'O'
        elif av >= 80:
            return 'E'
        elif av >= 70:
            return 'A'
        elif av >= 55:
            return 'P'
        elif av >= 40:
            return 'D'
        else:
            return 'T'


# This information is also uneditable. 
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()