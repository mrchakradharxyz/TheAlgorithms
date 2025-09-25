"""
Stack implementation using singly linked list data structure.
Provides basic stack operations: push, pop, peek, size, and display.
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

"""
createNode: Creates and returns a Node with data
Usage:
    node = createNode(10)
"""
def createNode(data) -> Node:
    return Node(data)

"""
push: Pushes (adds) an element to the top of the stack
Usage:
    stack = push(data, stack)
Returns:
    New head of the stack with the new node added
"""
def push(data, head: Node) -> Node:
    new_node = Node(data)
    new_node.next = head
    return new_node

"""
pop: Removes the top element from the stack
Usage:
    stack = pop(stack)
Returns:
    New head of the stack after popping the top
"""
def pop(head: Node) -> Node:
    if head is None:
        print("Stack Underflow")
        return None
    return head.next

"""
peek: Returns the top element of the stack without removing it
Usage:
    top = peek(stack)
"""
def peek(head: Node):
    if head is None:
        print("Stack is empty")
        return None
    return head.data

"""
size: Returns the number of elements in the stack
Usage:
    n = size(stack)
"""
def size(head: Node) -> int:
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

"""
display: Prints all elements in the stack from top to bottom
Usage:
    display(stack)
"""
def display(head: Node):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("EOL")
