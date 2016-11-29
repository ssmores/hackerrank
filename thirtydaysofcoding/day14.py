"""30 days of coding for HackerRank.


Day 14: Scope
by blondiebytes

Objective
Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

The absolute difference between two integers, a and b, is written as |a-b|. The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in elements.

The Difference class is started for you in the editor. It has a private integer array (elements) for storing N non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

Task
Complete the Difference class by writing the following:

    A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
    A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

Input Format

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in 2 lines of input; the first line contains N, and the second line describes the elements array.

Constraints
1 <= N <= 10
1 <= elements[i] <= 100, where 0 <= i <= N -1

Output Format

You are not responsible for printing any output; the Solution class will print the value of the maximumDifference instance variable.

Sample Input

3
1 2 5

Sample Output

4

Explanation
The scope of the elements array and maximumDifference integer is the entire class instance. The class constructor saves the argument passed to the constructor as the elements instance variable (where the computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any 2 elements: 
|1-2| = 1
|1-5| = 4
|2-5| = 3

The maximum of these differences is 4, so it saves the value 4 as the maximumDifference instance variable. The locked stub code in the editor then prints the value stored as maximumDifference, which is 4.

**************
Featured solutions 

Your constructor must save the argument passed as its integer array parameter to the integer array instance variable (elements).

The computeDifference method must then access the the integer array instance variable (elements) and find its maximum and minimum elements. Once these are found, the method must save their absolute difference to the maximumDifference instance variable.

Note: The use of Math.abs is not really necessary. Because the problem constraints stipulate that we are only dealing with positive numbers, max - min will always be positive.

Alternate Method
A different, more efficient way of finding the maximum absolute difference would to be to iterate through the elements and track the smallest and largest elements, then compute their difference: 




**************
"""
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    # Initial attempt, which runs, but has a runtime of O(n^2). No bueno.
    # def computeDifference(self):
    #     """Finds the maximum absolute difference in elements."""
    #     self.maximumDifference = 0
    #     maximumDifference = 0
    #     for i in range(len(self.__elements) - 1):
    #         for j in range(len(self.__elements)):
    #             diff = (self.__elements[i] - self.__elements[j])
    #             if diff < 0: 
    #                 diff = -diff
    #             self.maximumDifference = max(selfmaximumDifference, diff)
    #     return maximumDifference
    def computeDifference(self):
        """Finds the maximum absolute difference in elements."""
        small_n = self.__elements[0]
        largest_n = self.__elements[0]
        for item in self.__elements:
            if item < small_n:
                small_n = item
            elif item > largest_n:
                largest_n = item
        self.maximumDifference = largest_n - small_n
        return self.maximumDifference


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference