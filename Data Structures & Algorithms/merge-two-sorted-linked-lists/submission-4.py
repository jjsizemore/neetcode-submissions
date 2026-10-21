# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive approach
        # base case, 1 list None: return other list
        # handle rest first, then self
        # pointer saves smaller listnode
        # recursive case recurses on the next value for the smaller listnode
        # point saved listnode next ptr at recurse result
        # return saved listnode

        if not list1:
            return list2
        if not list2:
            return list1

        cur = None
        other = None
        if list1.val <= list2.val:
            cur = list1
            other = list2
        else:
            cur = list2
            other = list1
        
        cur.next = self.mergeTwoLists(cur.next, other)

        return cur