# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution, define recursing function addNumbers(self, l1, l2, carry) -> Optional[ListNode]
        # base case l1 & l2 None & carry 0 -> return None
        # divmod sum for node val & carry, set node.next to recursive call on l1.next, l2.next, carry
        # return node
        return self.addNumbers(l1, l2, 0)

    def addNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        carry, val = divmod(val1 + val2 + carry, 10)

        next_node = self.addNumbers(
            l1.next if l1 else None, 
            l2.next if l2 else None, 
            carry
            )

        new_node = ListNode(val, next_node)

        return new_node
