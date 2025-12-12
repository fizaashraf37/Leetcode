# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def countPath(root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            
            left_count = countPath(root.left)
            right_count = countPath(root.right)
            left_subtree_count = right_subtree_count = 0
            
            if root.left and root.val == root.left.val:
                left_subtree_count = left_count + 1
            if root.right and root.val == root.right.val:
                right_subtree_count = right_count + 1
            if (root.left and root.right) and (root.val == root.left.val and root.val == root.right.val):
                self.max_count = max(self.max_count, left_subtree_count + right_subtree_count)
            self.max_count = max(self.max_count, left_subtree_count, right_subtree_count)
            
            return max(left_subtree_count, right_subtree_count)
        
        self.max_count = 0
        countPath(root)

        return self.max_count
            