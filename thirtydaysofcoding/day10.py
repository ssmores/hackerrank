"""30 days of coding for HackerRank.

Day 10: Binary Numbers
by AvimanyuSingh


Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format
A single integer, n.

Constraints
1 <= n <= 10^5

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5

Sample Output 1

1

Sample Input 2

13

Sample Output 2

2

Explanation

Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.

**************
Featured solutions 
Python 2

To start out, we must convert n to a binary string. Then, we must find the largest number of consecutive ones. Here are a few approaches:

    1. Iterate through each character in the binary string and keep a running count of consecutive 1's.
    2. Split the binary string using as a delimiter, which results in an array of substrings having one or more consecutive 1's. We then find the length of the longest string in this array of consecutive-1 substrings; here are 2 approaches:
        1. Compare the individual lengths of each string in the array and keeping a running maximum. Then print your running maximum.
        2. Sort the array and print the length of the last string in the sorted array. This works because the lexicographical sorting of strings only composed of a single character ("1") will simply sort them by ascending length, meaning that the longest string is guaranteed to be the last element in the array.


**************
"""
#!/bin/python

import sys


n = int(raw_input().strip())
def b_convert(n):
    """Converting a base-10 interger into a binary/base-2 interger."""

    if n == 0:
        remainder = ''
        return remainder

    if n > 0:
        remainder = n % 2
        n = n/2
        return b_convert(n) + str(remainder)


def count_one(word):
    """Counting consecutive initial 1 values."""
    max_count = 0
    current = 0
    has_changed = False

    for i in range(len(word)):
        if word[i] == '1':
            current += 1
        else:
            max_count = max(max_count, current)
            current = 0
            has_changed = True

    if has_changed and max_count > current:
        print max_count
    else:
        print current


word = b_convert(n)
count_one(word)



