class Deque:
    
    def __init__(self):
        self.left = None
        self.right = None

    def isEmpty(self) -> bool:
        return not self.left and not self.right

    def append(self, value: int) -> None:
        new_node = Node(value, before = self.right)
        if self.right:
            self.right.after = new_node
            self.right = new_node
        else:
            self.left = new_node
            self.right = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value, after = self.left)
        if self.left:
            self.left.before = new_node
            self.left = new_node
        else:
            self.left = new_node
            self.right = new_node

    def pop(self) -> int:
        if not self.right:
            return -1
        res = self.right.val
        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.right = self.right.before
            self.right.after = None
        return res

    def popleft(self) -> int:
        if not self.left:
            return -1
        res = self.left.val
        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.left = self.left.after
            self.left.before = None
        return res
        
class Node:

    def __init__(self, val: int, before = None, after = None):
        self.val = val
        self.before = before
        self.after = after