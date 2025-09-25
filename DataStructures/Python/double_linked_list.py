from typing import Any, Optional

class Node:
    def __init__(self, data: Any, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def traverse(self) -> None:
        cur = self.head
        while cur:
            print(cur.data, end=" <=> ")
            cur = cur.next
        print("NULL")

    def traverse_reverse(self) -> None:
        cur = self.head
        if not cur:
            print("NULL")
            return
        while cur.next:
            cur = cur.next
        while cur:
            print(cur.data, end=" <=> ")
            cur = cur.prev
        print("NULL")

    def add_at_top(self, data: Any) -> None:
        newNode = Node(data, prev=None, next=self.head)
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def add_at_end(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        newNode = Node(data, prev=cur, next=None)
        cur.next = newNode

    def insert_after(self, after_value: Any, data: Any) -> None:
        cur = self.head
        while cur:
            if cur.data == after_value:
                newNode = Node(data, prev=cur, next=cur.next)
                if cur.next:
                    cur.next.prev = newNode
                cur.next = newNode
                return
            cur = cur.next
        print(f"Value {after_value} not found")

    def delete_at_top(self) -> None:
        if not self.head:
            return
        tmp = self.head
        self.head = tmp.next
        if self.head:
            self.head.prev = None
        del tmp  # free node

    def delete_at_end(self) -> None:
        if not self.head:
            return
        if not self.head.next:
            del self.head
            self.head = None
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None
        del cur

    def delete_by_value(self, data: Any) -> None:
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                del cur
                return
            cur = cur.next
        print(f"Value {data} not found")

    def free_all(self) -> None:
        """ Free the entire list """
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            del cur
            cur = nxt
        self.head = None
        print("List freed completely.")
