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
    public int MaxDepth(TreeNode root) {
        if (root == null) return 0;

        int depth = 0;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);

        while (q.Count > 0) {
            depth++;
            int levelSize = q.Count;

            for (int i = 0; i < levelSize; i++) {
                var cur = q.Dequeue();

                if (cur.left != null) q.Enqueue(cur.left);
                if (cur.right != null) q.Enqueue(cur.right);
            }
        }
        return depth;
    }
}
