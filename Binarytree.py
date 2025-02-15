# Node class represents each node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data  # Store the node's value
        self.left = None  # Pointer to the left child (initially None)
        self.right = None  # Pointer to the right child (initially None)

# BinaryTree class to manage the tree structure
class BinaryTree:
    def __init__(self):
        self.root = None  # Initially, the tree is empty (no root node)

    # Function to insert a node to the left of a given parent node
    def insertLeft(self, parent, value):
        if parent.left is None:  # If the left child is empty, place new node directly
            parent.left = Node(value)
        else:  
            # If left child already exists, push it down and insert the new node on top
            newNode = Node(value)
            newNode.left = parent.left  # The existing left child becomes the left child of the new node
            parent.left = newNode  # The new node becomes the parent's left child

    # Function to insert a node to the right of a given parent node
    def insertRight(self, parent, value):
        if parent.right is None:  # If right child is empty, place new node directly
            parent.right = Node(value)
        else:
            # If right child already exists, push it down and insert the new node on top
            newNode = Node(value)
            newNode.right = parent.right  # The existing right child becomes the right child of the new node
            parent.right = newNode  # The new node becomes the parent's right child

    # Function to print the tree structure (rotated 90 degrees for visualization)
    def printTree(self, node, level=0):
        if node is not None:  # Base condition for recursion: stop if node is None
            self.printTree(node.right, level + 1)  # Recursively print right subtree
            print("   " * level + str(node.data))  # Print the current node with indentation
            self.printTree(node.left, level + 1)  # Recursively print left subtree

# Example: Creating a simple binary tree
tree = BinaryTree()  # Initialize an empty binary tree
tree.root = Node(1)  # Create the root node with value 1

tree.insertLeft(tree.root, 2)  # Insert node 2 as the left child of root
tree.insertRight(tree.root, 3)  # Insert node 3 as the right child of root
tree.insertLeft(tree.root.left, 4)  # Insert node 4 as the left child of node 2
tree.insertRight(tree.root.left, 5)  # Insert node 5 as the right child of node 2

# Print the tree structure
tree.printTree(tree.root)
