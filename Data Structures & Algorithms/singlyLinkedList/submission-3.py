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
        i = 0

        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        
        return -1

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
        prev = self.dummy
        cur = self.dummy.next
        i = 0

        while cur:
            if i == index:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                self.length -= 1
                return True
            i += 1
            prev = cur
            cur = cur.next

        return False

    def getValues(self) -> List[int]:
        res = []
        cur = self.dummy.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
