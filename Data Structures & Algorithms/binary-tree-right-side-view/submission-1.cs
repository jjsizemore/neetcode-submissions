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
    public List<int> RightSideView(TreeNode root) {
        if (root == null) return new List<int>();

        var q = new Queue<TreeNode>();
        q.Enqueue(root);

        var retVal = new List<int>();

        while (q.Count > 0) {
            int lvlCount = q.Count;
            int rightmost = 0;

            for (int i = 0; i < lvlCount; i++) {
                var cur = q.Dequeue();
                rightmost = cur.val;

                if (cur.left != null) q.Enqueue(cur.left);
                if (cur.right != null) q.Enqueue(cur.right);
            }
            retVal.Add(rightmost);
        }

        return retVal;
    }
}
