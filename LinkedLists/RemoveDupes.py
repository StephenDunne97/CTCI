"""
Author: Stephen Dunne
Problem set: Linked Lists
Problem title: Remove duplicate values
Problem Description:  Write code to remove duplicates from an unsorted linked list.
Challenge: How would you solve this if an extra buffer was not allowed? 
"""


# Implementing your own LinkedList from scratch
class LinkedList: 
    def __init__(self, nodes = None):
        self.head = None # Marks the start of the LinkedList
        if nodes is not None: # If the LinkedList is initiated with data for each node
            node = Node(data=nodes.pop(0)) # Get first entered node
            self.head = node # Set first node to head
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self): # Iterates over and prints each node in the list. Without this, the "for node in llist_with_data" line will not run.
        node = self.head
        while node is not None:
            yield node # Yield is similar to return
            node = node.next 

class Node:
    def __init__(self, data):
        self.data = data # The data stored in the nde 
        self.next = None # The next node in the list
    
    def __repr__(self): # Special method used to represent a class's objects as a string.
        return self.data

# Problem: Write code to remove duplicates from an unsorted linked list.
# Challenge: How would you solve this if an extra buffer was not allowed? 

llist = LinkedList(['f','o','l','l','o','w','u','p',])
