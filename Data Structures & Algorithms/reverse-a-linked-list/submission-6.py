# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the rest then fix the pointer for the current node
        # base case empty list return None
        # recurse on head.next
        # fix head.next.next to point at head
        # set head.next to None to avoid cycles and return val returned by deepest recursive call

        if not head:
            return None

        new_head = head

        if head.next:   
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return new_head
