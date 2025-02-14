#delete nodes at the beginning

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

    def deleteAtBeginning(self):
        if self.head: # check if the list is not empty
            self.head = self.head.next #move to the next node

    def printList(self):
        current = self.head
        while current:
            print(current.data,end="-->")
            current = current.next
        print("NULL")

ls = LinkedList()
ls.insertAtBeginning(10)
ls.insertAtBeginning(20)
ls.insertAtBeginning(30)
ls.deleteAtBeginning()
ls.printList()

