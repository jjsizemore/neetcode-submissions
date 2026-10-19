class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        self._insert_between(new_node, self.tail.prev, self.tail)

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        self._insert_between(new_node, self.head, self.head.next)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self._remove(self.tail.prev)

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self._remove(self.head.next)

    def _remove(self, node: Node) -> int:
        res = node.val
        node.prev.next = node.next
        node.next.prev = node.prev
        return res

    def _insert_between(self, node: Node, prev: Node, next: Node):
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

