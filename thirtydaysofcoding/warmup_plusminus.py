"""Warmup questions from HackerRank.


Plus Minus
by vatsalchanana

Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Input Format

The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers describing an array of numbers (a0, a1, a2, ..., an-1).

Output Format

You must print the following 3 lines:

    A decimal representing of the fraction of positive numbers in the array.
    A decimal representing of the fraction of negative numbers in the array.
    A decimal representing of the fraction of zeroes in the array.


Sample Input

6
-4 3 -9 0 4 1         

Sample Output

0.500000
0.333333
0.166667

Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are 3/6 = 0.500000, 2/6 = 0.333333, and 1/6 = 0.166667, respectively.  

**************
Featured solutions
Python 2

no answer given. discussion included list comprehension functions...

**************
"""
#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def plus_minus(n, arr):
    """Takes number N and a list N long. Outputs decimal of positive, negative, and zero values in list."""

    pos = 0
    neg = 0
    zero = 0

    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    print '{:.6f}'.format(float(pos) / n)
    print '{:.6f}'.format(float(neg) / n)
    print '{:.6f}'.format(float(zero) / n)

plus_minus(n, arr)