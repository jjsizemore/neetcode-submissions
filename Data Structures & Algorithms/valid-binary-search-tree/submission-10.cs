/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    // Can traverse the tree iteratively with BFS & a queue
    public bool IsValidBST(TreeNode root) {
        if (root == null) return true;

        var q = new Queue<(TreeNode node, int left, int right)>();

        q.Enqueue((root, int.MinValue, int.MaxValue));

        while (q.Count > 0) {
            var (node, left, right) = q.Dequeue();

            if (node.val <= left || node.val >= right) return false;

            if (node.left != null)
                q.Enqueue((node.left, left, node.val));
            if (node.right != null)
                q.Enqueue((node.right, node.val, right));
        }

        return true;
    }
}
