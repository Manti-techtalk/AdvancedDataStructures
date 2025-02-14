#insert  new nodes at the beginning in Linked Lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

ls = LinkedList()

ls.insertAtBeginning(10)
