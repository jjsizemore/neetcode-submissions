class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.dummy.next

        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        self.length += 1
        new_head = ListNode(val, self.dummy.next)
        self.dummy.next = new_head

        # For case where list was empty
        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.length += 1
        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        cur = self.dummy

        for _ in range(index):
            cur = cur.next

        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next

        self.length -= 1

        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.dummy.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
