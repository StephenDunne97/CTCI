class LinkedList:
    def __init__(self, nodes=None):
        self.head = None  # Marks the start of the LinkedList
        if nodes is not None:  # If the LinkedList is initiated with data for each node
            node = Node(data=nodes.pop(0))  # Get first entered node
            self.head = node  # Set first node to head
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):  # Used to represent the exact string representation of the object
        node = self.head  # First node in the LinkedList
        nodes = []
        # None indicates that the last node in the list has been reached.
        while node is not None:
            # Take the data from the current node and append to nodes list
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    # Iterates over and prints each node in the list. Without this, the "for node in llist_with_data" line will not run.
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node  # Yield is similar to return
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    # Special method used to represent a class's objects as a string.
    def __repr__(self):
        return self.data


llist = LinkedList(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# If size is known


def sizeKnown(size, k, llist):
    jumps = size-k - 1  # -1 to account for 0 indexing
    count = 0
    current = llist.head

    while count != jumps:
        current = current.next
        count += 1

    print(current)


sizeKnown(10, 5, llist)
