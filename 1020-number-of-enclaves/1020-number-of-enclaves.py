class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(row: int, col: int):

            if grid[row][col] == 0:
                return

            grid[row][col] = 0

            for direction in directions:
                r, c = row + direction[0], col + direction[1] 
                
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    dfs(r,c)
        
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        count = 0

        for r in range(rows):
            for c in range(cols):
                count += grid[r][c]
            
        return count