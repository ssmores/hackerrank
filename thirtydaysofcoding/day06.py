"""30 days of coding for HackerRank.


Day 6: Let's Review
by AllisonP

Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Constraints
1 <= T <= 10
2 <= length of S <= 1000

Output Format

For each String Sj (where 0 <= j <= T -1 ), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.  

Sample Input

2
Hacker
Rank

Sample Output

Hce akr
Rn ak

Explanation

Test Case 0: S = "Hacker"
S[0] = 'H'
S[1] = 'a'
S[2] = 'c'
S[3] = 'k'
S[4] = 'e'
S[5] = 'r'

The even indices are 0, 2, 4, and the odd indices are 1, 3, 5. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from S's even indices (Hce), and the second string contains the ordered charactesr from S's odd indices (akr).

Test Case 1: S = 'Rank'
S[0] = 'R'
S[1] = 'a'
S[2] = 'n'
S[3] = 'k'

The even indices are 0 and 2, and the odd indices are 1 and 3. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from S's even indices (Rn), and the second string contains the ordered charactesr from S's odd indices (ak).


**************
Featured solutions 
Python 2

t = int(raw_input())
for _ in range(t):
    line = raw_input()
    first = ""
    second = ""

    for i, c in enumerate(line):
        if (i & 1) == 0:
            first += c
        else:
            second += c
    print first, second


**************
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input().strip())

for i in xrange(T):
    T_temp = map(str,raw_input().strip())
    evens = ''
    odds = ''
    for j in xrange(len(T_temp)):
        if j % 2 == 0 or j == 0:
            evens += T_temp[j]
        else:
            odds += T_temp[j]
    print evens, odds


