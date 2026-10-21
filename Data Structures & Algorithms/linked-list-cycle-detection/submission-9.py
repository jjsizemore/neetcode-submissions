# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # iterative with 2 pointers for space savings
        # slow and fast pointer
        # while slow and fast.next, check if slow == fast
        # if they are, return true, else slow = slow.next and fast = fast.next.next
        # if loop exits, fast hit none rather than cycling so return false
        if not head or not head.next:
            return False
            
        slow = head
        fast = head.next

        while slow and fast.next if fast else False:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        
        return False