"""Warmup questions from HackerRank.


Diagonal Difference
by vatsalchanana

Given a square matrix of size N x N, calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, N. The next N lines denote the matrix's rows, with each line containing N space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output
15

Explanation:
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, . The next lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Explanation
The primary diagonal is:
11
    5
        -12
Sum across the primary diagonal is 11 + 5 - 12 = 4

The secondary diagonal is:
        4
    5
10
Sum across the second diagonal: 4 + 5 + 10 = 19
Difference:|4-19| = 15




**************
Featured solutions
Python 2

size = input()
matrix = []

# reading input
for _ in xrange(size):
    row = map(int, raw_input().split())
    matrix.append(row)

# initialize s1 for right diagonal and s2 for left diagonal
s1, s2 = 0, 0

# summing up together in just 1 loop, -ve index
# (-x) in python is actually (size - x)
for i in xrange(size):
    s1 += matrix[i][i]
    s2 += matrix[-i-1][i]

# printing absolute difference
print abs(s1 - s2)

**************
"""
#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

def d_diff(n, a):
    """Sum values across diagonals, subtract the second from the first, provide absolute value."""

    p_diag = 0
    s_diag = 0

    for i in range(n):
        p_diag += a[i][i]
        s_diag += a[i][n - (i + 1)]

    diff = p_diag - s_diag

    if diff < 0:
        print -diff
    else:
        print diff

d_diff(n,a)