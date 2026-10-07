/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        // Injecting nodes after original allows us to complete the copy in one pass
        // Space O(1)
        // Time O(n)

        // Step 1: Inject new nodes
        var cur = head;

        while (cur != null)
        {
            var next = cur.next;
            cur.next = new Node(cur.val);
            cur.next.next = next;
            cur = cur.next.next;
        }

        // Step 2: Connect new nodes to new randoms
        cur = head;

        while (cur != null)
        {
            if (cur.random != null)
            {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        
        // Step 3: Extract new nodes
        var oldNode = head;
        var newNode = head.next;
        var newHead = head.next;

        while (oldNode != null)
        {
            oldNode.next = oldNode.next.next;
            newNode.next = newNode.next?.next;

            oldNode = oldNode.next;
            newNode = newNode.next;
        }

        return newHead;
    }
}
