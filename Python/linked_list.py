class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def traverse(node: Node):
    cur = node
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("NULL")


def add_at_end(data, node):
    new_node = Node(data)
    if not node:
        return new_node
    tmp = node
    while tmp.next:
        tmp = tmp.next
    tmp.next = new_node
    return node


def add_at_top(data, node):
    new_node = Node(data)
    new_node.next = node
    return new_node


def add_at_pos(data, pos_data, node):
    tmp = node
    while tmp:
        if tmp.data == pos_data:
            new_node = Node(data)
            new_node.next = tmp.next
            tmp.next = new_node
            return node
        tmp = tmp.next
    return node


def delete_at_top(node):
    if not node:
        return None
    return node.next


def delete_at_end(node):
    if not node:
        return None
    if not node.next:
        return None
    tmp = node
    while tmp.next.next:
        tmp = tmp.next
    tmp.next = None
    return node


def delete_at_pos(pos_data, node):
    if not node:
        return None
    if node.data == pos_data:
        return node.next
    tmp = node
    while tmp.next:
        if tmp.next.data == pos_data:
            tmp.next = tmp.next.next
            return node
        tmp = tmp.next
    print(f"Node with data {pos_data} not found")
    return node


def free_all(node):
    while node:
        tmp = node.next
        node.next = None
        node = tmp
    return None
