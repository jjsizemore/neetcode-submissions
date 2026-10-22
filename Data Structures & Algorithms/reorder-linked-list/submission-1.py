# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # iterate through the list, adding nodes to a stack
        # len(stack) // 2 = num nodes from stack that need to be injected
        # in a for loop, start with dummy.next = head, cur = dummy, cur = cur.next, temp = cur.next, cur.next = stack.pop(), cur = cur.next, cur.next = temp, 

        if not head.next:
            return
        
        stack = []
        res = head

        while head:
            stack.append(head)
            head = head.next
        
        l, r = 0, len(stack) - 1

        while l < r:
            stack[l].next = stack[r]
            l += 1
            stack[r].next = stack[l]
            r -= 1

        stack[l].next = None
