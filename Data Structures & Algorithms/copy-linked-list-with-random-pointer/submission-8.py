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

        cur = head.next

        while cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return head.next

# Time O(n)
# Space O(1)