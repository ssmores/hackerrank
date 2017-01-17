"""30 days of coding for HackerRank.

Day 23: BST Level-Order Traversal

Objective 
Today, we're going further with Binary Search Trees. Check out the Tutorial tab for learning materials and an instructional video!

Task 
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a BST: 
The first line contains an integer, T (the number of test cases). 
The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.

Output Format

Print the  value of each node in the tree's level-order traversal as a single line of  space-separated integers.

Sample Input

6
3
5
4
7
2
1
Sample Output

3 2 5 1 4 7 
Explanation

The input forms the following binary search tree: 

        3       Level 0
       / \
      2   5     Level 1
     /   / \
    1   4   7   Level 2



We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. The resulting level-order traversal is 3 --> 2 --> 5 --> 1 --> 4 --> 7, and we print these data values as a single line of space-separated integers.

**************
Featured solutions 

Python 2

    def levelOrder(self, root):
        traversal = ''
        
        if root != None:
            queue = [root]
            while len(queue) != 0:
                traversal += str(queue[0].data) + ' '
                if queue[0].left != None:
                    queue.append(queue[0].left)
                if queue[0].right != None:
                    queue.append(queue[0].right)
                queue.pop(0)
        print(traversal)


**************
"""
#Uneditable information
import sys

class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root


    #My solution here:
    def levelOrder(self,root):
         """Breadth search tree method. Prints tree from left to right."""

        to_visit = [root]

        while to_visit:
            current = to_visit.pop(0)
            if current.left and current.right:
                to_visit.extend([current.left, current.right])
            elif current.left:
                to_visit.append(current.left)
            elif current.right:
                to_visit.append(current.right)
            print current.data,


#Uneditable information
T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)
