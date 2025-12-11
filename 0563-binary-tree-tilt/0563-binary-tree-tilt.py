# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> int:

            if not root:
                return 0, 0
        
            nodes_sum_left, diff_sum_left = dfs(root.left)
            nodes_sum_right, diff_sum_right = dfs(root.right)
            nodes_sum = root.val + nodes_sum_left + nodes_sum_right
            diff_sum = abs(nodes_sum_left - nodes_sum_right) + diff_sum_left + diff_sum_right

            return nodes_sum, diff_sum
        
        _, diff_sum = dfs(root)
        return diff_sum





        

        