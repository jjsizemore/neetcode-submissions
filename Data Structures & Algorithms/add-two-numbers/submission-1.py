# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node pointing at first (ones spot) node
        # while both lists have valid nodes, add them; take ones spot for current result node and keep tens spot for next node addition
        # if only one list left, iterate through that node and clear out any carried digits

        dummy = ListNode()
        carry = 0
        cur = dummy

        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            carry = cur_sum // 10
            cur.next = ListNode(cur_sum % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            cur_sum = l1.val + carry
            carry = cur_sum // 10
            cur.next = ListNode(cur_sum % 10)
            cur = cur.next
            l1 = l1.next
        
        while l2:
            cur_sum = l2.val + carry
            carry = cur_sum // 10
            cur.next = ListNode(cur_sum % 10)
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)
            carry = 0

        return dummy.next