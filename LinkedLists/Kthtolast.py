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

class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    def __repr__(self):  # Special method used to represent a class's objects as a string.
        return self.data

def sizeKnown(size, k, llist): # If LinkedList size is known
    jumps_required = size-k - 1  # -1 to account for 0 indexing
    jumps_performed = 0
    current_node = llist.head

    while jumps_performed != jumps_required:
        current_node = current_node.next
        jumps_performed += 1

    print(current_node)

def main():
    llist = LinkedList(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    llist2 = LinkedList(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17'])
    sizeKnown(10, 5, llist)
    sizeKnown(17,3,llist2)

if __name__ ==  "__main__":
    main()