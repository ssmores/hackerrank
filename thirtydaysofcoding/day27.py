"""30 days of coding for HackerRank.

Day 27: Testing

Objective 
This challenge is very different from the others we've completed because it requires you to generate a valid test case for a problem instead of solving the problem. There is no input to read, you simply have to generate and print test values for the problem that satisfy both the problem's Input Format and the criteria laid out in the Task section. Check out the Tutorial tab for an instructional video on testing!

Consider the following problem (but do not solve it):

Problem Statement

A Discrete Mathematics professor has a class of N students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than k students are present when class starts. Given the arrival time of each student, determine if the class is canceled.
Input Format

The first line of input contains t, the number of lectures.
The information for each lecture spans two lines. The first line has two space-separated integers, n (the number of students in the class) and k (the cancelation threshold). The second line contains n space-separated integers describing the array of students' arrival times (A = a0, a1, ..., an-1).

Note: Non-positive arrival times (ai <= 0) indicate the student arrived early or on time; positive arrival times (ai > 0) indicate the student arrived ai minutes late. If a student arrives exactly on time ai = 0, the student is considered to have entered before the class started.

Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.
Example

When properly solved, this input:
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Produces this output:
YES
NO
For the first test case, . The professor wants at least  students in attendance, but only  arrive on time (and ). Thus, the class is canceled.

For the second test case, . The professor wants at least  students in attendance, and  do arrive on time (and ). Thus, the class is not canceled.


Task

Create and print a test case for the problem above that meet the following criteria:
t <= 5
1 <= n <= 200
1 <= k <= n
-10^3 <= ai <= 10^3 where i contained in [1, n]
The value of n must be distinct across all the test cases. 
Array A must have at least 1 zero, 1 positive integer, and 1 negative integer.


Scoring

If you submit x correct test cases, you will earn (20 * x%) of the maximum score. You must submit 5 test cases to earn the maximum possible score.

Input Format

You are not responsible for reading anything from stdin.

Output Format

Print 11 lines of output that can be read by the Professor challenge as valid input. Your test case must result in the following output when fed as input to the Professor challenge's solution:

YES
NO
YES
NO
YES


Explanation

Your code must print lines of output that follow the Input Format in the Professor challenge above. For example, this partial solution to this challenge:

print('2')
print('4 3')
print('-1 -3 4 2')
print('5 2')
print('0 -1 2 1 4')

prints the following output that can be used as valid input for the Professor challenge:

2
4 3
-1 -3 4 2
5 2
0 -1 2 1 4

When read by a valid solution to the Professor challenge, it produces the following output:

YES
NO
You must do something similar to this, except that the test case you develop must meet the constraints set in the Task section above.

**************
Featured solutions 

Python 3




**************
"""

print 5
print '5 4'
print '-1 5 1 2 3'
print '5 2'
print '0 -1 -3 4 5'
print '6 3'
print '-2 5 -3 1 2 3'
print '10 7'
print '-10 0 4 10 2 -2 -7 -2 -9 -3'
print '20 18'
print '3 5 -9 -1 0 0 0 0 -3 -4 -7 1 0 0 -3 -4 -1 0 -2 -1 0'
