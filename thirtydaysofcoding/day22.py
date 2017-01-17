"""30 days of coding for HackerRank.

Day 22: Binary Search Trees

Objective 
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

Task 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, n, denoting the number of nodes in the tree. 
Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7
Sample Output

3
Explanation

The input forms the following BST:

        3
       / \
      2   5
     /   / \
    1   4   6
             \
              7



The longest root-to-leaf path is shown below:
3 --> 5 --> 6 --> 7



There are 4 nodes in this path that are connected by 3 edges, meaning our BST's height = 3. Thus, we print 3 as our answer.

**************
Featured solutions 

Python 2

def getHeight(self, root):
    if root == None:
        return -1
    else:
        return 1 + max( self.getHeight(root.left), self.getHeight(root.right) )


**************
"""
#Uneditable information
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
    def getHeight(self,root):
        """Returns height of longest branch from further leaf."""

        #base case
        #if the node doesn't have a left or a right attribute, then you're reached end branch
        if root.right is None and root.left is None:
            return 0

        if root.left is None:
            return 1 + self.getHeight(root.right)
        elif root.right is None:
            return 1 + self.getHeight(root.left)
        else:
            left_height = 1 + self.getHeight(root.left)
            right_height = 1 + self.getHeight(root.right)
            return max(left_height, right_height)


#Uneditable information
T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root,data)
height = myTree.getHeight(root)
print height 



