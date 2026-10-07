/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        // Two Pointers (1 pass)

        // Use a dummy node to handle edge cases
        var dummy = new ListNode(0, head);
        var slow = dummy;
        var fast = dummy;

        // Move fast pointer n + 1 ahead
        for (int i = 0; i <= n; i++)
        {
            fast = fast.next;
        }

        // Iterate both pointers until fast = null
        while (fast != null)
        {
            slow = slow.next;
            fast = fast.next;
        }
        
        // Slow pointer will be pointing at node to remove
        slow.next = slow.next.next;

        return dummy.next;
    }
}
