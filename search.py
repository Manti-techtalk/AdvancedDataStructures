class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        """Insert a new node at the start."""
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def deleteAtStart(self):
        """Delete the first node."""
        if self.head:
            self.head = self.head.next

    def tranvserse(self):
        """Print all the nodes in the list."""
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("NULL")

    def search(self, target):
        """Search for a node with a specific value."""
        current = self.head
        while current:
            if current.data == target:
                return True  # Target found
            current = current.next
        return False  # Target not found

# Example usage:
ls = LinkedList()
ls.insertAtStart(10)
ls.insertAtStart(20)
ls.insertAtStart(30)
ls.insertAtStart(40)

# Search for an element
found = ls.search(40)
if found:
    print("Element found!")
else:
    print("Element not found!")

# Traverse the list and print all elements
ls.tranvserse()
