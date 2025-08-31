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
    cur = node
    while cur.next:
        cur = cur.next
    cur.next = new_node
    return node


def add_at_top(data, node):
    return Node(data, node)


def add_at_pos(data, pos, node):
    """Insert at index `pos` (0-based)."""
    if pos == 0:
        return add_at_top(data, node)

    cur = node
    idx = 0
    while cur and idx < pos - 1:
        cur = cur.next
        idx += 1

    if not cur:
        print(f"Position {pos} out of range")
        return node

    cur.next = Node(data, cur.next)
    return node


def delete_at_top(node):
    return node.next if node else None


def delete_at_end(node):
    if not node or not node.next:
        return None
    cur = node
    while cur.next and cur.next.next:
        cur = cur.next
    cur.next = None
    return node


def delete_at_pos(pos, node):
    if not node:
        return None
    if pos == 0:
        return node.next

    cur = node
    idx = 0
    while cur.next and idx < pos - 1:
        cur = cur.next
        idx += 1

    if cur.next:
        cur.next = cur.next.next
    else:
        print(f"Position {pos} out of range")
    return node


def free_all(node):
    while node:
        tmp = node.next
        node.next = None
        node = tmp
    return None
