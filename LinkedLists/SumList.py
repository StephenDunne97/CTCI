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


class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the nde
        self.next = None  # The next node in the list

    # Special method used to represent a class's objects as a string.
    def __repr__(self):
        return self.data


def extractValues(llist):
    buff = []
    num1 = []
    num2 = []
    for node in llist:
        if node.next != None:
            if node.data == '+':
                continue
            elif node.next.data == '+':
                buff.append(node.data)
                num1 = buff
                buff = num2
            else:
                buff.append(node.data)
        else:
            buff.append(node.data)
            num2 = buff

    result = [num1, num2]
    return result


def processNums(numberlist):
    numberlist.reverse()
    result = int("".join(map(str, numberlist)))
    return result


def main():
    llist = LinkedList([7, 1, 6, '+', 5, 9, 2])
    nums = extractValues(llist)
    num1 = processNums(nums[0])
    num2 = processNums(nums[1])
    print(num1)
    print(num2)


if __name__ == "__main__":
    main()
