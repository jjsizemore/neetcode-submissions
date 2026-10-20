# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []

        while head:
            stack.append(head)
            head = head.next

        dummy = ListNode(next = stack[-1])
        cur = dummy
        
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None

        return dummy.next