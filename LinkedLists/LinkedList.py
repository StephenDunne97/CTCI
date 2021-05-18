class Node():
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class SLinkedList():
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    # Insert Node at the beginning of list
    def AtBeginning(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def AtEnd(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
    
    def InBetween(self, midNode, data):
        if midNode is None:
            print("The middle node does not exist.")
            return  
        NewNode = Node(data)
        NewNode.next = midNode.next
        midNode.next = NewNode
    
    def RemoveNode(self, Removekey):
        Head = self.head
        if (Head is not None and Head.data == Removekey):
            self.head=Head.next
            Head = None
            return
        
        while (Head is not None):
            if Head.data == Removekey:
                break
            prev = Head
            Head = Head.next 
        
        if (Head == None):
            return
        
        prev.next == Head.next 
        Head = None


    


linkedy = SLinkedList() # Instantiating the Linked List
linkedy.head = Node("Mon") # Setting Headval to a node object with a dataval of "Mon"
e2 = Node("Tue") # Instantiating a Node object with dataval "Tue"
e3 = Node("Wed") # Instantiating a Node object with dataval "Wed"
linkedy.head.next = e2
e2.next = e3
linkedy.AtBeginning("Sun")
linkedy.InBetween(e2, "Doge")
linkedy.AtEnd("Thur")




linkedy.listprint()
