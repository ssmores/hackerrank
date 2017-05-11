"""HackerRank Algorithm Problems.

The Maximum Subarray

Given an array A = {a1, a2, ..., an} of N elements, find the maximum possible sum of a

1. Contiguous subarray
2. Non-contiguous (not necessarily contiguous) subarray.

Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer T. T cases follow. 
Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

Constraints
1 <= T <= 10
1 <= N <= 10^3
-10^4 <= a <= 10^4

The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input

2 
4 
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output

10 10
10 11

Explanation

In the first case: 
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case: 
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum. 
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.



**************
Featured solutions 
Python 2




**************
"""

T = int(raw_input().strip())

for i in xrange(T):
    lst_len = int(raw_input())
    new_a = map(int, raw_input().split(' '))

    # For max continuous subarray (Kadane's algorithm).
    max_current = max_global = new_a[0]

    # For non-continuous subarray max sum.
    non_cont_sum = 0
    max_num = new_a[0]

    sum1 = 0
    sum2 = new_a[0]
    sum3 = max(sum1, sum2)

    for j in xrange(lst_len):
        # Kadane's algorithm for max subarray sum
        if j >= 1:
            max_current = max(new_a[j], max_current + new_a[j])
            if max_current > max_global:
                max_global = max_current

        # Non continuous sum
        if new_a[j] > 0:
            non_cont_sum += new_a[j]
            has_changed = True

        if new_a[j] > max_num:
            max_num = new_a

    if non_cont_sum == 0:
        non_cont_sum = max_num



        # # Calculuation for non-continuous sums
        # if j == 1 and non_cont_sum < 0:
        #     if new_a[j] > non_cont_sum:
        #         non_cont_sum = new_a[j]
        #         max_num = new_a[j]
        # elif new_a[j] < min_num:
        #     min_num = new_a[j]
        # elif new_a[j] < max_num and new_a[j] + non_cont_sum > non_cont_sum:
        #     non_cont_sum += new_a[j]
        # else:
        #     non_cont_sum += new_a[j]
        #     max_num = new_a[j]

    print max_global, non_cont_sum



