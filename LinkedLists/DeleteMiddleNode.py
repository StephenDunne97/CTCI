class LinkedList:
    def __init__(self, nodes=None):
        self.head = None  # Marks the start of the LinkedList
        if nodes is not None:  # If the LinkedList is initiated with data for each node
            node = Node(data=nodes.pop(0))  # Get first entered node
            self.head = node  # Set first node to head
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __iter__(self): # Iterates over and prints each node in the list. Without this, "for node in llist" will not run.
        node = self.head
        while node is not None:
            yield node  # Yield is similar to return
            node = node.next

    def remove_node(self, target_node_data): # Remove method edited to not use a "previous_node" variable
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:  # If head is the node to be removed
            raise Exception("You cannot remove the head.")

        for node in self:
            if node.data == target_node_data and node.next == None:
                raise Exception("You cannot remove the tail.")
            elif node.data == target_node_data:
                node.data = node.next.data
                node.next = node.next.next
                return

        raise Exception("Node with data '%s' not found." % target_node_data)

class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    def __repr__(self): # Special method used to represent a class's objects as a string.
        return self.data

def main():
    llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
    llist.remove_node('a')
    for node in llist:
        print(node) 

if __name__ == "__main__":
    main()