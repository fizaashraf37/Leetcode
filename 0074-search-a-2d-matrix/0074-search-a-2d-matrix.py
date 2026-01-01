class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        first_row, last_row = 0, len(matrix)-1
        mid_row = 0

        while first_row <= last_row:
            mid_row = first_row + (last_row - first_row) // 2
            if target < matrix[mid_row][0]:
                last_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                first_row = mid_row + 1
            else:
                break

        low, high = 0, len(matrix[0])-1

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid_row][mid] == target:
                return True
            if target < matrix[mid_row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
        

        
        