"""HackerRank Algorithm Problems.

Nikita and the Game

Nikita just came up with a new array game. The rules are as follows:

Initially, there is an array, A, containing N integers.

In each move, Nikita must partition the array into 2 non-empty contiguous parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets 1 point; otherwise, the game ends.

After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array A.

Nikita loves this game and wants your help getting the best score possible. Given A, can you find and print the maximum number of points she can score?



Input Format

The first line contains an integer, T, denoting the number of test cases. Each test case is described over 2 lines in the following format:

A line containing a single integer, N, denoting the size of array A.
A line of N space-separated integers describing the elements in array A.

Constraints
1 <= T <= 10
1 <= N <= 2^14
0 <= A(i) <= 10^9

Scoring

1 <= N <= 2^8 for 30 percent of the test data
1 <= N <= 2^11 for 60 percent of the test data
1 <= N <= 2^14 for 100 percent of the test data

Output Format

For each test case, print Nikita's maximum possible score on a new line.

Sample Input

3
3
3 3 3
4
2 2 2 2
7
4 1 0 1 1 0 1
Sample Output

0
2
3


Explanation

Test Case 0:

Nikita cannot partition A into 2 parts having equal sums. Therefore, her maximum possible score is 0 and we print 0 on a new line.

Test Case 1:

Initially, A looks like this:

    2 2 2 2

She splits the array into 2 partitions having equal sums, and then discards the left partition:

    (discard 2 2) 2 2

She then splits the new array into 2 partitions having equal sums, and then discards the left partition: 
    
    (discard 2) 2

At this point the array only has 1 element and can no longer be partitioned, so the game ends. Because Nikita successfully split the array twice, she gets 2 points and we print 2 on a new line.

**************
Featured solutions 
Python 2



**************
"""

#!/bin/python

import sys


def points(arr, arr_total):
    """Number of times to split an array with equal sums on each side."""

    if len(arr) == 1:
        return 0
    if arr_total % 2 > 0:
        return 0
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 0

    half = arr_total / 2
    curr_total = 0

    for i in xrange(len(arr)):
        if curr_total < (half):
            curr_total += arr[i]
        else:
            break
        
    to_i = len(arr[:i])
    after_i = len(arr[i:])


    if to_i < after_i:
        arr = arr[i:]
    else:
        arr = arr[:i]
    

    return 1 + points(arr, half)

T = int(raw_input().strip())
for i in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().strip().split(' '))

    A_sum = 0
    for num in A:
        A_sum += num

    print points(A, A_sum)



