"""HackerRank Algorithm Problems.

Apple and Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where s is the start point and t is the end point. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a and the orange tree is at point b.


When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.


Input Format

The first line contains two space-separated integers denoting the respective values of s and t. 
The second line contains two space-separated integers denoting the respective values of a and b. 
The third line contains two space-separated integers denoting the respective values of m and n. 
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a. 
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Constraints
1 <= s, t, a, b, m, n <= 10^5
-10^5 <= d <= 10^5
a < s < t < b


Output Format

Print two lines of output:

On the first line, print the number of apples that fall on Sam's house.
On the second line, print the number of oranges that fall on Sam's house.
Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6
Sample Output 0

1
1
Explanation 0

The first apple falls at position 5 - 2 = 3. 
The second apple falls at position 5 + 2 = 7. 
The third apple falls at position 5 + 1 = 6. 
The first orange falls at position 15 + 5 = 20. 
The second orange falls at position 15 - 6 = 9. 
Only one fruit (the second apple) falls within the region between 7 and 11, so we print 1 as our first line of output. 
Only the second orange falls within the region between 7 and 11, so we print 1 as our second line of output.

**************
Featured solutions 
Python 2

start_house, end_house = map(int, raw_input().split())
left_tree, right_tree = map(int, raw_input().split())
number_of_apples, number_of_orranges = map(int, raw_input().split())
apple_distances = map(int, raw_input().split())
orange_distances = map(int, raw_input().split())
apple_count = 0
orange_count = 0

for distance in apple_distances:
    if start_house <= left_tree + distance <= end_house:
        apple_count += 1
for distance in orange_distances:
    if start_house <= right_tree + distance <= end_house:
        orange_count += 1
print apple_count
print orange_count


Alternative answers:
print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

print(sum([1 for each in apple if s <= (each + a) <=t]))
print(sum([1 for each in orange if s <= (each + b) <=t]))

print(len([x for x in apple if s <= x+a <= t ]), len([y for y in orange if s <= y+b <= t ]),sep = '\n')

**************
"""
#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

a_count = 0
o_count = 0

for i in xrange(m):
    if a + apple[i] >= s and a + apple[i] <= t:
        a_count += 1

for j in xrange(n):
    if b + orange[j] <= t and b + orange[j] >= s:
        o_count += 1

print a_count
print o_count

