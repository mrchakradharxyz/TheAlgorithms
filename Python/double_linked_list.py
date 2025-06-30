from typing import Any

class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

def traverse(node: Node) -> None:
    cur = node
    while cur:
        print(f"{cur.data}",end="<=>")
        cur = cur.next
    print("NULL")

def addNodeAtTop(data, node: Node) -> Node:
    newNode = Node(data)
    newNode.prev = None
    newNode.next = node
    return newNode

def addNodeATEnd(data, node: Node) -> Node:
    newNode = Node(data=data)
    tmp = node
    while tmp.next:
        tmp = tmp.next
    tmp.next = newNode
    newNode.prev = tmp
    newNode.next = None
    return node

def addNodeAtPos(data, p1, p2, node: Node) -> Node:
    cur: Any = node
    while cur:
        if cur.data == p1 and cur.next is not None and cur.next.data == p2:
            newNode = Node(data=data)
            newNode.next = cur.next
            newNode.prev = cur
            cur.next.prev = newNode
            cur.next = newNode
            return node
        cur = cur.next
    return node

def deleteAtTop(node) -> Node:
    node = node.next
    return node

def deleteAtEnd(node: Node) -> Node:

    tmp: Any = node
    while tmp.next:
        tmp = tmp.next
    tmp.prev.next = None

    tmp.prev = None
    return node

def deleteAtPos(data, node: Node) -> Node:
    tmp: Any = node
    while tmp is not None:
        if tmp.data == data:
            if tmp.prev is not None:
                tmp.prev.next = tmp.next
            else:
                node = tmp.next
            if tmp.next is not None:
                tmp.next.prev = tmp.prev
            return node
        tmp = tmp.next
    return node


def main():
    n1 = Node(10)
    n2 = Node(20, prev=n1)
    n3 = Node(30, prev=n2)
    n1.next, n2.next = n2, n3
    updated = addNodeAtTop(1, n1)
    traverse(updated)
    updated = addNodeATEnd(40,n1)
    traverse(updated)
    updated = addNodeAtPos(15,10,20,n1)
    traverse(updated)
    updated = deleteAtTop(updated)
    traverse(updated)
    updated = deleteAtEnd(updated)
    traverse(updated)
    updated = deleteAtPos(30,updated)
    traverse(updated)
    updated = addNodeAtTop("Data", updated)
    traverse(updated)
    updated = deleteAtTop(updated)
    traverse(updated)

if __name__ == "__main__":
    main()
