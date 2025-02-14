#going through the linkedlist nodes to print its values

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def transverse(self):
        current = self.head

        while current:
            if current != None:
                print(current.data,end="->")
                current = current.next
            else:
                break
        print("NUll")
ls = LinkedList()
ls.insertAtBeginning(10)
ls.insertAtBeginning(20)
ls.insertAtBeginning(30)
ls.transverse()