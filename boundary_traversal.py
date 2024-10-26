# Python3 program for binary traversal of binary tree


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeaves(root: Node):
    if root:
        printLeaves(root.left)
        printLeaves(root.right)

        if not root.left and not root.right:
            print(root.data)


def printBoundaryLeft(root: Node):
    if root and root.left or root.right:
        print(root.data)
    if root.left:
        printBoundaryLeft(root.left)
    elif root.right:
        printBoundaryLeft(root.right)


def printBoundaryRight(root):
    if root.right:
        printBoundaryRight(root.right)
    elif root.left:
        printBoundaryRight(root.left)
    if root and root.left or root.right:
        print(root.data)


def printBoundary(root):
    if root:
        print(root.data)
        printBoundaryLeft(root.left)
        printLeaves(root)
        printBoundaryRight(root.right)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.right.right = Node(10)
root.left.left.left.right = Node(11)
root.right.right.right.left = Node(12)
root.left.left.left.right.right = Node(13)

# printBoundaryLeft(root.left)
printBoundary(root)
