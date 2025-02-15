# Stack implementation using a list (LIFO: Last In, First Out)
class Stack:
    def __init__(self):
        self.stack = []  # An empty list to store elements in the stack

    def push(self, data):  
        """Add an element to the top of the stack."""
        self.stack.append(data)

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.isEmpty():  
            return self.stack.pop()  # Removes and returns the last added element
        return "Stack is empty!!"

    def peek(self):
        """Return the top element without removing it."""
        if not self.isEmpty():
            return self.stack[-1]  # Returns the last element
        return "Stack is empty"

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def printStack(self):
        """Print the stack from top to bottom."""
        if not self.isEmpty():
            print("Top ->", " -> ".join(map(str, self.stack[::-1])), "-> Bottom")
        else:
            print("Stack is empty!")

# Testing the stack
stack = Stack()  # Initialize the stack
stack.push(10)
stack.push(20)
stack.push(30)

print("Peek:", stack.peek())  # Should return 30

stack.printStack()  
# Output: Top -> 30 -> 20 -> 10 -> Bottom

print("Popped:", stack.pop())  # Removes 30
stack.printStack()  
# Output: Top -> 20 -> 10 -> Bottom
