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
    def __init__(self, nodes = None):
        self.head = None # Marks the start of the LinkedList
        if nodes is not None: # If the LinkedList is initiated with data for each node
            node = Node(data=nodes.pop(0)) # Get first entered node
            self.head = node # Set first node to head
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self): # Used to represent the exact string representation of the object
        node = self.head # First node in the LinkedList
        nodes = []
        while node is not None: # None indicates that the last node in the list has been reached.
            nodes.append(node.data) # Take the data from the current node and append to nodes list
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    def __iter__(self): # Iterates over and prints each node in the list. Without this, the "for node in llist_with_data" line will not run.
        node = self.head
        while node is not None:
            yield node # Yield is similar to return
            node = node.next 

    def add_first(self, node):
        node.next = self.head # Setting the previous head to the next node in the list 
        self.head = node # Setting the head to the new node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            print(current_node.next)
            pass
        current_node.next = node

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

llist_with_data = LinkedList(['a','b','c','d','e'])
print(llist_with_data.__repr__())

llist_with_data.add_first(Node('X'))
llist_with_data.add_last(Node('Y'))

for node in llist_with_data:
    print(node)