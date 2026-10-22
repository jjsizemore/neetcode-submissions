# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # find midpoint
        # reverse second half
        # merge the two halves

        res = head
        midpoint = self._find_midpoint(head)

        # reverse: track prev and cur
        prev, cur = None, midpoint.next

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # merge list starting at prev with list starting at head
        second = prev
        midpoint.next = None

        while head and second:
            temp1 = head.next
            temp2 = second.next
            head.next = second
            second.next = temp1
            head = temp1
            second = temp2

        # [0,1,2,3]
        # [0,2,1,3]

    def _find_midpoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        #s  fs s. f     f. 
        [1, 2, 3, 4, 5, 6]
        #s  fs     f == None 
        [1, 2, 3]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow