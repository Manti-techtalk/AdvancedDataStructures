class Node:
    def __init__(self, data):  
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):  
        self.head = None  

    def insert(self, data):
        """Insert a new node at the beginning."""
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        """Print the linked list properly."""
        current = self.head
        while current:
            print(current.data, end=" --> ")  
            current = current.next
        print("NULL")  

# Test the linked list
ls = LinkedList()
ls.insert(10)
ls.insert(20)
ls.insert(30)

print("Linked List:")
ls.printList()  # Expected Output: 30 --> 20 --> 10 --> NULL























"""
Write a function to print the elements of a linked list in reverse order.
You are not allowed to modify the linked list (no reversing the pointers).

"""