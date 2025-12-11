class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        left_col = [n+1]*(n+1)
        right_col = [0]*(n+1)
        top_row = [0]*(n+1)
        bottom_row = [n+1]*(n+1)

        for x, y in buildings:
            left_col[y] = min(left_col[y], x)
            right_col[y] = max(right_col[y], x)
            top_row[x] = max(top_row[x], y)
            bottom_row[x] = min(bottom_row[x], y)
        
        count = 0
        for x, y in buildings:
            if left_col[y] < x < right_col[y] and bottom_row[x] < y < top_row[x]:
                count += 1
        
        return count








        

        