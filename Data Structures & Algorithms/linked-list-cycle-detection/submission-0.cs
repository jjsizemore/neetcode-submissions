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
    public bool HasCycle(ListNode head) {
        var slow = head;
        var fast = head?.next;

        while (slow != null && fast != null)
        {
            if (slow == fast)
                return true;
            slow = slow.next;
            fast = fast?.next?.next;
        }

        return false;
    }
}
