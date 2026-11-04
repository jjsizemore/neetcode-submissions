# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # simpler problem, reversing all the nodes in a list
        # keep a head node and a tail node, sandwiching the actual nodes of the list
        # iterate through the list keeping track of prev and cur
        # starting with head and head.next, reverse the links by keeping a temp ptr for the original cur.next
        # for k node groups, set up head & tail nodes that sandwich them, then perform the above algo, and then move head to tail and work on the next k
        # if you hit the end before getting to k nodes between head and tail, leave the nodes as is

        dummy = ListNode(0, head)
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        before_group = dummy

        for i in range(length // k):
            group_start = before_group.next

            # after_group will be node after each group
            after_group = group_start
            for _ in range(k):
                after_group = after_group.next
            
            prev = after_group
            cur = group_start

            while cur is not after_group:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            
            # prev is now first node of group
            # group_start is now last node of group
            before_group.next = prev

            # Old first node is now group's tail
            before_group = group_start
            
            
        return dummy.next
