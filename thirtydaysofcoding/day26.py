"""30 days of coding for HackerRank.

Day 26: Nested Logic

Objective 
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!

Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late).
3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (the number of months late)
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format

The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned. 
The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Constraints
1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000
It is guaranteed that the date will be valid Gregorian calendar date.

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Given the following return dates: 
Actual:  Da = 9, Ma = 6, Ya = 2015
Expected: De = 6, Me = 6, Ye = 2015

Because Ye = Ya, we know it is less than a year late. 
Because Me = Ma, we know it's less than a month late. 
Because De < Da, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be 15 Hackos x (# of days late). We then print the result of 15 x (Da - De) = 15 x (9 - 6) = 45 as our output.

**************
Featured solutions 

Python 3




**************
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = map(int,raw_input().strip().split(' '))
expected = map(int,raw_input().strip().split(' '))

def lib_fine(date_a, date_e):
    """Determine fine for overdue library book based on specified schedule."""

    
    if date_a[2] > date_e[2]:
        print 10000
    elif date_a[1] > date_e[1]:
        print (500 * (date_a[1] - date_e[1]))
    elif date_a[0] > date_e[0]:
        print (15 * (date_a[0] - date_e[0]))
    else:
        print 0


    # return fine

print lib_fine(actual, expected)
