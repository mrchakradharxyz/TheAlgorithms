"""
Circular Singly Linked List Implementation
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def createNode(data):
    return Node(data)

def insertAtTop(data, head):
    new_node = createNode(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        cur = head
        while cur.next != head:
            cur = cur.next
        cur.next = new_node
        new_node.next = head
        return new_node  # new head

def insertAtEnd(data, head):
    new_node = createNode(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        cur = head
        while cur.next != head:
            cur = cur.next
        cur.next = new_node
        new_node.next = head
        return head  # head doesn't change

def deleteAtTop(head):
    if head is None:
        print("List is empty")
        return None
    if head.next == head:
        return None  # only one node
    cur = head
    while cur.next != head:
        cur = cur.next
    cur.next = head.next
    return head.next  # new head

def deleteAtEnd(head):
    if head is None:
        print("List is empty")
        return None
    if head.next == head:
        return None
    cur = head
    prev = None
    while cur.next != head:
        prev = cur
        cur = cur.next
    prev.next = head
    return head

def display(head):
    if head is None:
        print("List is empty")
        return
    cur = head
    while True:
        print(cur.data, end=" -> ")
        cur = cur.next
        if cur == head:
            break
    print("(head)")


head = None
head = insertAtTop(10, head)
head = insertAtTop(20, head)
head = insertAtEnd(5, head)
head = insertAtEnd(1, head)

print("List after insertions:")
display(head)
head = deleteAtTop(head)
print("After deleting at top:")
display(head)
head = deleteAtEnd(head)
print("After deleting at end:")
display(head)
