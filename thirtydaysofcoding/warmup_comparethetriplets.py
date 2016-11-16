"""Warmup questions from HackerRank.


Compare the Triplets
by Shafaet

    Problem
    Submissions
    Leaderboard
    Discussions
    Editorial

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).

Your task is to find their comparison scores by comparing a0 with b0, a1 with b1, and a2 with b2.

    If ai > bi, then Alice is awarded 1 point.
    If ai < bi, then Bob is awarded 1 point.
    If ai = bi, then neither person receives a point.

Given A and B, can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective values in triplet A.
The second line contains 3 space-separated integers, b0, b1, and b2, describing the respective values in triplet B.

Constraints
1 <= ai <= 100
1 <= bi <= 100

Output Format
Print two space-separated integers denoting the respective comparison scores earned by Alice and Bob.


Sample Input

5 6 7
3 6 10

Sample Output
1 1

Explanation
In this example:
A = (a0, a1, a2) = (5, 6, 7)
B = (b0, b1, b2) = (2, 6, 10)

Now, let's compare each individual score:

    a0 > b0, so Alice receives point.
    a1 = b1, so nobody receives a point.
    a2 < b2, so Bob receives point.

Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we print 1 1 (Alice's comparison score followed by Bob's comparison score) on a single line. 
**************
Featured solutions
Python 2

a_triplet = map(int, raw_input().split())
b_triplet = map(int, raw_input().split())
alice_points = 0
bob_points = 0
for a_val, b_val in zip(a_triplet, b_triplet):
    if a_val < b_val:
        bob_points += 1
    elif a_val > b_val:
        alice_points += 1
print alice_points, bob_points

**************
"""

import sys


# a0,a1,a2 = raw_input().strip().split(' ')
# a0,a1,a2 = [int(a0),int(a1),int(a2)]
# b0,b1,b2 = raw_input().strip().split(' ')
# b0,b1,b2 = [int(b0),int(b1),int(b2)]

a_list = raw_input().strip().split(' ')
b_list = raw_input().strip().split(' ')



def comparison(a_list, b_list):
    """Compares the values of ai to bi and provides point assignments when one is larger."""

    a_tot = 0
    b_tot = 0
    a_len = len(a_list)

    for i in range(a_len):
        a_list[i] = int(a_list[i])
        b_list[i] = int(b_list[i])

        if a_list[i] > b_list[i]:
            a_tot += 1
        elif a_list[i] < b_list[i]:
            b_tot += 1

    print a_tot, b_tot
