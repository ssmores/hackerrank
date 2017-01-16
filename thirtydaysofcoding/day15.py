"""30 days of coding for HackerRank.


Day 15: Linked List
by harsha_s

Objective
Today we're working with Linked Lists. Check out the Tutorial tab for learning materials and an instructional video!

A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer data value that must be added to the end of the list as a new Node object. 

Task
Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: If the head argument passed to the insert function is null, then the initial list is empty.

Input Format

The insert function has 2 parameters: a pointer to a Node named head, and an integer value, data.
The constructor for Node has 1 parameter: an integer value for the data field.

You do not need to read anything from stdin.


Output Format

Your insert function should return a reference to the node of the linked list. 


Sample Input

The following input is handled for you by the locked code in the editor:
The first line contains T, the number of test cases.
The T subsequent lines of test cases each contain an integer to be inserted at the list's tail.
4
2
3
4
1

Sample Output

The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:

2 3 4 1



Explanation

T = 4, so the locked code in the editor will be inserting 4 nodes.
The list is initially empty, so head is null; accounting for this, our code returns a new node containing the data value 2 as the head of our list. We then create and insert nodes 3, 4, and 1 at the tail of our list. The resulting list returned by the last call to insert is [2,3,4,1], so the printed output is 2 3 4 1.

Initial: head --> null
T0: head -->Node n0(data = 2, next = null)
T1: head -->Node n0(data = 2, next = n1) -->Node n1(data = 3, next = null) 
T2: T3: head -->Node n0(data = 2, next = n1) -->Node n1(data = 3, next = n2) -->Node n2(data = 4, next = null)
T3: head -->Node n0(data = 2, next = n1) -->Node n1(data = 3, next = n2) -->Node n2(data = 4, next = n3) -->Node n3(data = 1, next = null) 

**************
Featured solutions 
Python 2




**************
"""
# This was uneditable.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  
    #This is where I can provide additional coding information.

    def insert(self,head,data):
        """Takes head and data as parameters, returns head of linked list."""

        if head is None:
            self.head = Node(data)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(data)

        return self.head




# This was provided and is uneditable.
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);




