# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first we have to count the number of elems in the list
        # index of node to remove will be len(list) - n
        # at node n - 1, we have to set its .next ptr to cur.next.next

        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        
        idx_to_remove = length - n

        dummy = ListNode(-1, head)
        cur = dummy

        while idx_to_remove > 0:
            idx_to_remove -= 1
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next