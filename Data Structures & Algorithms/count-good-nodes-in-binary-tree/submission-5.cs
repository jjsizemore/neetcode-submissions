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
        return dfs(root, root.val);
    }

    public int dfs(TreeNode root, int highest) {
        if (root == null) return 0;

        if (root.val >= highest) {
            highest = root.val;
            return dfs(root.left, highest) + dfs(root.right, highest) + 1;
        } else {
            return dfs(root.left, highest) + dfs(root.right, highest);
        }
    }
}
