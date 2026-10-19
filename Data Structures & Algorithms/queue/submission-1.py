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
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value, prev = self.head, next = self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        res = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return res

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        res = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return res
        
class Node:

    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next