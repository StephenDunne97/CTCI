# LinkedList implemented taken from: https://realpython.com/linked-lists-python/
# Practical Implementations of LinkedLists: queues/stacks/graphs.
from collections import deque # Deque (Deck) = Object from the collections module

""" 
Quick implementation of a LinkedList in Python using deque
LinkedList = deque("abcdef")
print(LinkedList)
LinkedList.append("g")
print(LinkedList)
print(LinkedList.pop())
print(LinkedList)
LinkedList.appendleft("Q")
print(LinkedList)
"""
# Implementing your own LinkedList from scratch
class LinkedList: 
    def __init__(self):
        self.head = None # Marks the start of the LinkedList
    
    def __repr__(self):
        node = self.head # First node in the LinkedList
        nodes = []
        while node is not None: # None indicates that the last node in the list has been reached.
            nodes.append(node.data) # Take the data from the current node and append to nodes list
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data # The data stored in the nde 
        self.next = None # The next node in the list
    
    def __repr__(self): # Special method used to represent a class's objects as a string.
        return self.data


llist = LinkedList()
node1 = Node("a")
llist.head = node1 # Setting the head of the LinkedList
node2 = Node("b")
node3 = Node("c")
node1.next = node2
node2.next = node3
print(llist.__repr__())