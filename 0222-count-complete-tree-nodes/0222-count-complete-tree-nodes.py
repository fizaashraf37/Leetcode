# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def findDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + findDepth(root.left)
        
        if not root:
            return 0

        left_depth = findDepth(root.left)
        right_depth = findDepth(root.right)

        if left_depth == right_depth:
            # left subtree is complete, so count left subtree nodes and recurse on right
            # subtree
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # right subtree is complete, so count right subtree nodes and recurse on left
            # subtree
            return (1 << right_depth) + self.countNodes(root.left)
        