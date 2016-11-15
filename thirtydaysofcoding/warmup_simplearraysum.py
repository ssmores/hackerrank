"""Warmup questions from HackerRank.


Simple Array Sum
by shashank21j

    Problem
    Submissions
    Leaderboard
    Discussions
    Editorial

Given an array of N integers, can you find the sum of its elements?

Input Format

The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11

Sample Output

31

Explanation

We print the sum of the array's elements, which is: 1 + 2 + 3 + 4 + 10 + 11 = 33.


#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

**************
Featured solutions
Python 2

number_of_elements = int(raw_input())
array = map(int, raw_input().split())
print sum(array)
**************
"""

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

sum = 0
for i in range(n):
    sum += arr[i]

print sum