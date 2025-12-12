# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = self.find_successor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        else:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    def find_successor(self, root: Optional[TreeNode]) -> TreeNode:
        
        successor = root.right
        while successor.left:
            successor = successor.left
        return successor
        
    
        

        