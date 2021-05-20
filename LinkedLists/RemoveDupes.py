"""
Author: Stephen Dunne
Problem set: Linked Lists
Problem title: Remove duplicate values
Problem Description:  Write code to remove duplicates from an unsorted linked list.
Challenge: How would you solve this if an extra buffer was not allowed?
"""


# Implementing your own LinkedList from scratch
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None  # Marks the start of the LinkedList
        if nodes is not None:  # If the LinkedList is initiated with data for each node
            node = Node(data=nodes.pop(0))  # Get first entered node
            self.head = node  # Set first node to head
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # Iterates over and prints each node in the list. Without this, the "for node in llist_with_data" line will not run.
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node  # Yield is similar to return
            node = node.next

    def remove_node(self, target_node_data, target_node_next):
        if self.head is None:
            raise Exception("List is empty")

        if self.head == target_node_data:  # If head is the node to be removed
            self.head = self.head.next  # The new head is the next node after the head
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data and node.next == target_node_next:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found." % target_node_data)


class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    # Special method used to represent a class's objects as a string.
    def __repr__(self):
        return self.data

# Problem: Write code to remove duplicates from an unsorted linked list.
# Challenge: How would you solve this if an extra buffer was not allowed?


"""
llist = LinkedList(['f', 'o', 'l', 'l', 'o', 'w', 'u', 'p'])

# Using a buffer
temp = []
for node in llist:
    if node.data in temp:
        llist.remove_node(node.data)
    else:
        temp.append(node.data)

for node in llist:  # The first O is removed because it is the first to be found when purging. The problem says nothing about this.
    print(node)

"""
# Not using a buffer

llist = LinkedList(['f', 'o', 'l', 'l', 'o', 'w', 'u', 'p'])

current = llist.head

while current.next:
    runner = current.next
    while runner.next:
        if current.data == runner.data:
            temp = runner.next
            llist.remove_node(runner.data, runner.next)
            runner = temp
        else:
            runner = runner.next
    current = current.next

for node in llist:
    print(node)