"""30 days of coding for HackerRank.


Day 7: Arrays
by saikiran9194

Objective
Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers describing array A's elements.

Constraints
1 <= N <= 1000
1 <= Ai <= 10000, where Ai is the ith integer in the array.

Output Format

Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input

4
1 4 3 2

Sample Output

2 3 4 1


**************
Featured solutions 
Python 2




**************
"""
#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in range(1, n + 1):
    print arr[-i],

