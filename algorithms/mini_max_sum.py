"""HackerRank Algorithm Problems.

Mini-Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

Each integer is in the inclusive range [1, 10^9].

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the following sums using four of the five integers:

If we sum everything except 1, our sum is 2 + 3 + 4 + 5 = 14.
If we sum everything except 2, our sum is 1 + 3 + 4 + 5 = 13.
If we sum everything except 3, our sum is 1 + 2 + 4 + 5 = 12.
If we sum everything except 4, our sum is 1 + 2 + 4 + 5 = 11.
If we sum everything except 5, our sum is 1 + 2 + 3 + 4 = 10.
As you can see, the minimal sum is 1 + 2 + 3 + 4 = 10 and the maximal sum is 2 + 3 + 4 + 5 = 14. Thus, we print these minimal and maximal sums as two space-separated integers on a new line.

Hints: Beware of integer overflow! Use 64-bit Integer.

**************
Featured solutions 
Python 2

First, let's make some observations:
We can minimize the sum by excluding the largest element from the sum.
We can maximize the sum by excluding the smallest element from the sum.
There are five integers, and the maximum value of each integer is 10^9. This means that, worst-case scenario, our final sum could be a maximum of 4 x 10^9 (which is outside of the bounds of an integer).
To solve this, we read in five elements; for each element:
Add the element to a running sum of all elements, sum.
If the element is less than the current minimum, min, set the element as the new current minimum.
If the element is greater than the current maximum, max, set the element as the new current maximum.
After checking all five elements, we have the following information:
The sum of five elements, sum.
The value of the smallest element, min.
The value of the largest element, max.
We then use this to calculate:
The minimum sum of four of the five elements is sum - max.
The maximum sum of four of the five elements is sum - min.


**************
"""

#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
total = 0
for num in arr:
    total += num

small_num = min(arr)
large_num = max(arr)

print (total - large_num), (total - small_num)

