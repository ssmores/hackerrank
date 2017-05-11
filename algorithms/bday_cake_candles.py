"""HackerRank Algorithm Problems.

Birthday Cake Candles

Colleen is turning n years old! She has n candles of various heights on her cake, and candle i has height height(i). Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height(i) for each individual candle, find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer, n, denoting the number of candles on the cake. 
The second line contains n space-separated integers, where each integer i describes the height of candle i.

Constraints
1 <= n <= 10^5
1 <= height(i) <= 10^7

Output Format

Print the number of candles Colleen blows out on a new line.

Sample Input 0

4
3 2 1 3

Sample Output 0

2

Explanation 0

We have one candle of height 1, one candle of height 2, and two candles of height 3. Colleen only blows out the tallest candles, meaning the candles where height = 3. Because there are 2 such candles, we print 2 on a new line.

**************
Featured solutions 
Python 2

There are two steps to solving this challenge:
Find the maximum height, m, of any candle.
Count the number of occurrences of candles having height = m among all the candles, then print this number.

n = input()
arr = map(int, raw_input().split())
print arr.count(max(arr))

**************
"""

#!/bin/python

import sys

n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
c_num = {}
max_amt = 0
#c_height = 0

for item in height:
    if item in c_num:
        c_num[item] += 1
        if c_num[item] > max_amt:
            max_amt = c_num[item]
            #c_height = item
    else:
        c_num[item] = 1
        if not max_amt:
            max_amt = 1
            #c_height = item

print max_amt


