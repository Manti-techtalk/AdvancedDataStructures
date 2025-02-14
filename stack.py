# uses the LIFO, Last In, First Out
#easy to implemet using a list
class Stack:
    def __init__(self):
        self.stack = [] #  an empy list that will store elements in stack

    def appendStack(self,data):
        self.stack.append(data) #similar to lists, you add by appending

    def remove(self):
        if not self.isEmpty(): # check if its empy or not
            self.stack.pop()
        return "Stack is empty!!"
    def peek(self): # to peek is to return the first element without removing it
        if not self.isEmpty():
            self.stack[-1]
        return "Stack is empty"
    def isEmpty(self):
        return len(self.stack) == 0
    def printstack(self):
        if not self.isEmpty():
            print("Top ->", " -> ".join(map(str, self.stack[::-1])), "-> Bottom")
        else:
            print("Stack is empty!")

stack = Stack()# initiallise the object from the class
stack.appendStack(10)
stack.appendStack(20)
stack.appendStack(30)
stack.peek()
stack.printstack()

