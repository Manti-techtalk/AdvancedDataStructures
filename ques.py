# Uses FIFO, first come first served type vibe
class Que:
    def __init__(self):
        self.que = []  # Initialize the queue

    def enque(self, data):  # Add an element to the end
        self.que.append(data)

    def deque(self):  # Remove an element from the front
        if not self.isEmpty():  # Corrected function call
            return self.que.pop(0)  # Index 0 to pop the first element
        return "Queue is empty"

    def isEmpty(self):  # Check if the queue is empty
        return len(self.que) == 0

    def peek(self):  # Return the front element without removing it
        if not self.isEmpty():
            return self.que[0]
        return None

    def printQue(self):  # Print queue elements
        if not self.isEmpty():
            print("Front ->", " -> ".join(map(str, self.que)), "-> Rear")
        else:
            print("Queue is empty!")

# Testing the queue
que = Que()
que.enque(10)
que.enque(20)
que.enque(30)
que.deque()  # Removes 10
que.printQue()  # Output: Front -> 20 -> 30 -> Rear
