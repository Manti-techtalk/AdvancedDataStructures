class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.data,end="->")
            self.count += 1
            current = current.next
        print("Null")
        print("There are ",self.count, "nodes")

    
ls = LinkedList()
ls.insert(10)
ls.insert(20)
ls.insert(30)
ls.printList()
