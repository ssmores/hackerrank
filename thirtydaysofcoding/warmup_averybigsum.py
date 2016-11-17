"""Warmup questions from HackerRank.

A Very Big Sum
by vatsalchanana


You are given an array of integers of size N. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

Input Format

The first line of the input consists of an integer N. The next line contains N space-separated integers contained in the array.

Output Format

Print a single value equal to the sum of the elements in the array.

Constraints
1 <= N <= 10
0 <= A[i] <= 10^10

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015

Note:
The range of the 32-bit integer is (-2^31) to (2^31 -1) or [-2147483648, 2147483647].

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int in C/C++ or long data type in Java to store such sums.


**************
Featured solutions
Python 2

n = int(raw_input().strip())
print sum(map(int, raw_input().strip().split(' ')))

**************
"""
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sum = 0
for item in arr:
    sum += item

print sum