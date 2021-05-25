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

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:  # Will run until the for loop raises a "StopIteration" exception
            pass
        current_node.next = node  # Set the next node of the last node to the new last node

class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    # Special method used to represent a class's objects as a string.
    def __repr__(self):
        return self.data

def main():
    original = LinkedList([3,5,8,5,10,2,1]) 
    x = 5
    lesser = LinkedList() # Contains nodes less than x
    greater = LinkedList() # Contains nodes greater than or equal to x

    for node in original:
        if node.data < x:
            lesser.add_last(Node(node.data))
        elif node.data >= x:
            greater.add_last(Node(node.data))
    
    combined = lesser
    combined.add_last(greater.head)

    for node in combined:
        print(node.data)

if __name__ == "__main__":
    main()