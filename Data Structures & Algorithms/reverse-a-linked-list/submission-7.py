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

        # Sets up the head return from deepest call
        new_head = head

        # If not the deepest, reset new_head pointer to point at deepest return value, then set next pointer for the level below to point to cur head
        if head.next:   
            new_head = self.reverseList(head.next)
            head.next.next = head

        # Value is set by the caller layer above, at top layer this value must be None to avoid circle
        head.next = None

        return new_head
