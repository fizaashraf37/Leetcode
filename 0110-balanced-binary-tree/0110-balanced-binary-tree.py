# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        _, is_balanced = self.find_depth(root)
        return is_balanced

    def find_depth(self, root: Optional[TreeNode]):

        if not root:
            return 0, True
        
        left_height, is_balanced_left = self.find_depth(root.left)
        if not is_balanced_left:
            return left_height, False
        right_height, is_balanced_right = self.find_depth(root.right)
        root_height = max(left_height, right_height) + 1
        if abs(left_height - right_height) > 1 or not is_balanced_right:
            return root_height, False

        return root_height, True
        