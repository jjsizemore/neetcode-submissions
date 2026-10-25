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
        # two passes, one to copy the nodes & form a map from old to new
        # another to set the random pointers in the new list based on the old

        if not head:
            return

        dummy = Node(-1, head)
        cur = dummy
        to_new = {}

        while cur:
            to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = dummy

        while cur:
            to_new[cur].next = to_new[cur.next] if cur.next else None
            to_new[cur].random = to_new[cur.random] if cur.random else None
            cur = cur.next

        return to_new[dummy.next]
