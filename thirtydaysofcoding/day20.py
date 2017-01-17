"""30 days of coding for HackerRank.

Objective 
Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}

Task 
Given an array, a, of size n containing distinct elements a[0], a[1], ..., a[n-1], sort array  in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:

1.  Array is sorted in numSwaps swaps. 
where numSwaps is the number of swaps that took place.

2. First Element: firstElement 
where firstElement is the first element in the sorted array.

3. Last Element: lastElement 
where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, n, denoting the number of elements in array a. 
The second line contains n space-separated integers describing a, where the ith integer is a[i], all i in set [0, n-1].

Constraints
2 <= n <= 600

1 <= =a[i] <= 2 x 10^6, all i in set [0, n-1] 

Output Format

There should be 3 lines of output:

1.  Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
 
where firstElement is the first element in the sorted array.
 
where lastElement is the last element in the sorted array.

Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

Explanation

Sample Case 1: 
The array is already sorted, so 0 swaps take place and we print the necessary 3 lines of output shown above.

Sample Case 2: 
The array is not sorted, and its initial values are: {3, 2, 1}. The following 3 swaps take place:
1. {3, 2, 1} --> {2, 3, 1}
2. {2, 3, 1} --> {2, 1, 3}
3. {2, 1, 3} --> {1, 2, 3}



At this point the array is sorted and we print the necessary 3 lines of output shown above.


**************
Featured solutions 

Python 3

import sys

n = int(input())
a = [int(i) for i in input().strip().split(' ')]
numSwaps = 0

for i in range(n):
    currentSwaps = 0

    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            currentSwaps += 1
            numSwaps += 1
            
    if currentSwaps == 0:
        break
        
print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))




**************
"""
#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

swap_count = 0
for i in range(n):
    if i == n - 1:
        break
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j] 
            swap_count += 1

print 'Array is sorted in {} swaps.'.format(swap_count)
print 'First Element: {}'.format(a[0])
print 'Last Element: {}'.format(a[-1])


