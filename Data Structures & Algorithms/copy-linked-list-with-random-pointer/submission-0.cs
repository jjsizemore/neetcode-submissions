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
        Dictionary<Node, Node> map = new();

        var cur = head;
        while (cur != null)
        {
            Node copy = new Node(cur.val);
            map[cur] = copy;
            cur = cur.next;
        }

        cur = head;

        while (cur != null)
        {
            var copy = map[cur];
            copy.next = cur.next != null ? map[cur.next] : null;
            copy.random = cur.random != null ? map[cur.random] : null;

            cur = cur.next;
        }
        return head != null ? map[head] : null;
    }
}
