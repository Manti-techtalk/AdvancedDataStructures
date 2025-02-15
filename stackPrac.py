class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def append(self,value):
        self.stack.append(value)

    def remove(self):
        if not self.isEmpty():
            self.stack.pop()
        return "The stack is empty"
    def peek(self):
        if not self.isEmpty():
            self.stack[-1]
        return "Stack is empty"
    def reverse(self):
        if not self.isEmpty():
            current = self.stack[0]
            new = current[::-1]
            print(new)

stack = Stack()
stack.append("hello")
stack.reverse()

