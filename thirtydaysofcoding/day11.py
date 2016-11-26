"""30 days of coding for HackerRank.


Day 11: 2D Arrays
by Shafaet

Objective
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a 6 x 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglass in A, and an hourglass sum is the sum of an hourglass' values. 

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in will be in the inclusive range of -9 to 9.

Constraints
-9 <= A[i][j] <= 9
0 <= i,j <= 5

Output Format
Print the largest (maximum) hourglass sum found in A. 

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4



**************
Featured solutions 
Python 2




**************
"""

#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

def max_hg(matrix):
    """Intakes a 6x6 matrix and return sum of max hourglass."""

    max_sum = None
    current_sum = None
    # for i, row in enumerate(matrix[-2]):
    #     for j, num in row[:-2]:

    # Can only go through the top 4 rows.
    # Can only go through the first 4 values in each row.

    for i in range(len(matrix)):
        if i < 4: 
            for j in range(len(matrix[i])):
                if j < 4: 
                    current_sum = (matrix[i][j] +
                                   matrix[i][j+1] +
                                   matrix[i][j+2] +
                                   matrix[i+1][j+1] +
                                   matrix[i+2][j] +
                                   matrix[i+2][j+1] +
                                   matrix[i+2][j+2])
                    
                    if max_sum is None:
                        max_sum = current_sum
                    else: 
                        max_sum = max(max_sum, current_sum)

    print max_sum

max_hg(arr)

                     
            


