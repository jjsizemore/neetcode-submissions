# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # break the the problem down into a simpler one: merge 2 sorted lists
        # for k lists, merge adjacent lists
        # instead of taking all the nodes and sorting them, which requires O(n log (n)) time
        # this approach takes O(log k) rounds, each one processing up to n nodes
        
        if not lists:
            return

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                j = i + 1
                if j == len(lists):
                    mergedLists.append(lists[i])
                    break
                
                mergedList = self._mergeSortedLists(lists[i], lists[j])
                mergedLists.append(mergedList)

            lists = mergedLists

        return lists[0]

    def _mergeSortedLists(self, l1, l2):
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2
        
        return dummy.next


