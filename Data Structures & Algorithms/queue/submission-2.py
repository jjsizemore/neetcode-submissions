def _remove(node: Node) -> None:
    node.prev.next = node.next
    node.next.prev = node.prev

def _insert_between(node: Node, prev: Node, next: Node):
    node.prev = prev
    node.next = next
    prev.next = node
    next.prev = node

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value, prev = self.tail.prev, next = self.tail)
        _insert_between(new_node, self.tail.prev, self.tail)

    def appendleft(self, value: int) -> None:
        new_node = Node(value, prev = self.head, next = self.head.next)
        _insert_between(new_node, prev = self.head, next = self.head.next)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        res = self.tail.prev.val
        _remove(self.tail.prev)
        return res

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        res = self.head.next.val
        _remove(self.head.next)
        return res
        
class Node:

    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next