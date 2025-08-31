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
        return head  # head remains same

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

def deleteByValue(head, value):
    if head is None:
        print("List is empty")
        return None
    if head.data == value:
        return deleteAtTop(head)

    prev, cur = head, head.next
    while cur != head:
        if cur.data == value:
            prev.next = cur.next
            return head
        prev, cur = cur, cur.next

    print(f"Value {value} not found.")
    return head

def free_all(head):
    if head is None:
        print("List is already empty")
        return None
    cur = head.next
    while cur != head:
        nxt = cur.next
        cur.next = None
        cur = nxt
    head.next = None
    print("All nodes freed")
    return None

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
    print(f"({head.data} is head)")
