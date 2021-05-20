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

    def add_first(self, node):
        node.next = self.head  # Setting the previous head to the next node in the list
        self.head = node  # Setting the head to the new node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:  # Will run until the for loop raises a "StopIteration" exception
            pass
        current_node.next = node  # Set the next node of the last node to the new last node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found." % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head == target_node_data:  # If head is the node to be removed
            self.head = self.head.next  # The new head is the next node after the head
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
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


llist = LinkedList(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# If size is known
size = 10
k = 5
jumps = size-k - 1  # -1 to account for 0 indexing
count = 0
current = llist.head

while count != jumps:
    current = current.next
    count += 1

print(current)
