# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:

            if not node:
                return 0
            
            left_count = dfs(node.left, node)
            right_count = dfs(node.right, node)
            
            count = 0
            if node.left and not node.left in visited:
                count += 1
                if node.right:
                    visited.add(node.right)
                visited.add(node)
                visited.add(parent)
            if node.right and not node.right in visited:
                count += 1
                visited.add(node.right)
                visited.add(node)
                visited.add(parent)

            return left_count + right_count + count 

        visited = set()
        count = dfs(root, None) 
        if root not in visited:
            count += 1
        return count 

            
            
