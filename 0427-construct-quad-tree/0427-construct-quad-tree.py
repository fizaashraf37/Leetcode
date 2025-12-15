"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)
        return self.constructQuadTree(0, 0, n, grid)

    def constructQuadTree(self, r: int, c: int, n: int, grid: List[List[int]]):
        
        is_uniform = self.isUniform(r, c, n, grid)
        if is_uniform:
            return Node(grid[r][c], True, None, None, None, None)
        
        s = n//2 
        root = Node(grid[r][c], False, None, None, None, None)
        root.topLeft = self.constructQuadTree(r, c, s, grid)
        root.topRight = self.constructQuadTree(r, c+s, s, grid)
        root.bottomLeft = self.constructQuadTree(r+s, c, s, grid)
        root.bottomRight = self.constructQuadTree(r+s, c+s, s, grid)

        return root
        
    
    def isUniform(self, r: int, c: int, n: int, grid: List[List[int]]) -> bool:

        first_cell = grid[r][c]

        for i in range(r+1, r+n):
            for j in range(c , c+n):
                if grid[i][j] != grid[r][c]:
                    return False
        
        return True