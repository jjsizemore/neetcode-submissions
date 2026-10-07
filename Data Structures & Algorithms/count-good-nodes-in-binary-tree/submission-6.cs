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
    public int GoodNodes(TreeNode root) {
        return Dfs(root, root.val);
    }

    public int Dfs(TreeNode node, int max) {
        if (node == null) return 0;

        int res = node.val >= max ? 1 : 0;
        max = Math.Max(node.val, max);
        res += Dfs(node.left, max) + Dfs(node.right, max);
        return res;
    }
}
