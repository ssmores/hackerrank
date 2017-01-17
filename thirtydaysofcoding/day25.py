"""30 days of coding for HackerRank.

Day 25: Running Time and Complexity

Objective 
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task 
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(n^0.5) primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, T, the number of test cases. 
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
1 <= T <= 30
1 <= n <= 2 x 10^9


Output Format

For each test case, print whether n is Prime or Not prime on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: n = 12. 
12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 6), so we print Not prime on a new line.

Test Case 1: n = 5. 
5 is only divisible 1 and itself, so we print Prime on a new line.

Test Case 2: n = 7. 
7 is only divisible 1 and itself, so we print Prime on a new line.

**************
Featured solutions 

Python 3

import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);




**************
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input().strip())

for i in xrange(T):
    n = int(raw_input())
    largest_int = int(n**0.5)

    if n == 1:
        print "Not prime"
    elif n == 2:
        print "Prime"
    else:
        for j in xrange(2, largest_int + 1):
            if n % j == 0:
                print "Not prime"
                break
            else:
                print "Prime"


