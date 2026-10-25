"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(1) extra space solution
        # insert copied nodes after originals in one pass
        # then we can use the fact that the new nodes are predictably after their originals to map random pointers
        # then we can remove the originals and return head.next

        if not head:
            return

        dummy = Node(-1, head)

        cur = head

        while cur:
            ptr = cur.next
            cur.next = Node(cur.val, ptr)
            cur = ptr

        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        res_dummy = head.next

        cur_old = head
        cur_new = head.next

        while cur_new:
            cur_old.next = cur_new.next
            cur_old = cur_old.next
            cur_new.next = cur_old.next if cur_old else None
            cur_new = cur_new.next

        return res_dummy

# Time O(n)
# Space O(1)