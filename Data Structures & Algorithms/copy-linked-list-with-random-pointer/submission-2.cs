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
        // Two passes
        // 1: Create LL & old->new map
        // 2: Copy rand pointers using map

        var dict = new Dictionary<Node, Node>();
        var cur = head;
        while (cur != null)
        {
            dict.Add(cur, new Node(cur.val));
            cur = cur.next;
        }

        cur = head;
        while (cur != null)
        {
            var clone = dict[cur];

            clone.next = cur.next != null ? dict[cur.next] : null;
            clone.random = cur.random != null ? dict[cur.random] : null;
            cur = cur.next;
        }

        return dict[head];
    }
}
