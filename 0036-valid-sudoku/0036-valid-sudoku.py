class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_row_valid(row: int) -> bool:
            visited = [False]*9
            for col in range(9):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])-1
                if visited[num]:
                    return False
                visited[num] = True
            
            return True
        
        def is_col_valid(col: int) -> bool:
            visited = [False]*9
            for row in range(9):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])-1
                if visited[num]:
                    return False
                visited[num] = True
            
            return True
        
        def is_subbox_valid(row: int, col: int) -> bool:
            visited = [False]*9
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == ".":
                        continue
                    num = int(board[r][c])-1
                    if visited[num]:
                        return False
                    visited[num] = True
            
            return True

        for i in range(9):
            if not is_row_valid(i):
                return False
            if not is_col_valid(i):
                return False
        
        for row in range(3):
            for col in range(3):
                if not is_subbox_valid(row*3, col*3):
                    return False
        
        return True
        

        