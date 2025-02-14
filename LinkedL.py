class Node:  # Train car
    def __init__(self, data):
        self.data = data  # Store the value
        self.next = None  # Pointer to the next car

class LinkedList:  # Train system
    def __init__(self):
        self.head = None  # Start with no train cars

    def insert(self, data):
        """
        Insert a new node at the beginning of the list.
        The new node becomes the new head.
        """
        newNode = Node(data)  # Create a new train car
        newNode.next = self.head  # Link new car to the old engine
        self.head = newNode  # Update the head to be the new car

    def delete(self):
        """
        Delete the first node (engine).
        If the list is empty, do nothing.
        """
        if self.head is not None:  # If there is at least one node
            self.head = self.head.next  # Move the engine to the next car

    def search(self, target):  # Fixed spelling mistake
        """
        Search for a node with a specific value.
        Returns True if found, False otherwise.
        """
        current = self.head  # Start from the engine
        while current:
            if current.data == target:  # If we find the target
                return True
            current = current.next  # Move to the next car
        return False  # Not found

    def printList(self):
        """
        Print all elements in the Linked List.
        """
        current = self.head  # Start from the first car
        while current:
            print(current.data, end=" → ")  # Print value
            current = current.next  # Move to the next node
        print("NULL")  # End of the train

# Testing the linked list
ls = LinkedList()
ls.insert(5)
ls.insert(10)
ls.insert(15)

print("Linked List after inserting elements:")
ls.printList()  # Expected Output: 15 → 10 → 5 → NULL

ls.delete()
print("Linked List after deleting head:")
ls.printList()  # Expected Output: 10 → 5 → NULL

# Searching for values
print("Is 10 in the list?", ls.search(10))  # Expected Output: True
print("Is 100 in the list?", ls.search(100))  # Expected Output: False
