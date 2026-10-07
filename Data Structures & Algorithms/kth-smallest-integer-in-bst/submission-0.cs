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
    private int count;
    private int retVal;
    
    // Constraints:
    // 0 <= Node.val <= 1000
    // 1 <= k <= The number of nodes in the tree <= 1000

    public int KthSmallest(TreeNode root, int k) {
        // DFS - inorder traverse
        dfs(root, k);
        return this.retVal;
    }

    // returns true if node is found
    private bool dfs(TreeNode node, int k) {
        if (node == null) return false;

        if (dfs(node.left, k)) return true;

        count++;

        if (count == k) {
            retVal = node.val;
            return true;
        }

        return dfs(node.right, k);
    }
}
