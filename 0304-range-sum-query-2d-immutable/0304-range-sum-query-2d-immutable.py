class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = self.computePrefixSum(matrix)
    
    def computePrefixSum(self, matrix: List[List[int]]):

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j-1 >= 0:
                    matrix[i][j] += matrix[i][j-1]
                if i-1 >= 0:
                    matrix[i][j] += matrix[i-1][j]
                    if j-1 >= 0:
                        matrix[i][j] -= matrix[i-1][j-1]
        
        return matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        region_sum = self.matrix[row2][col2]
        if col1-1 >= 0:
            region_sum -= self.matrix[row2][col1-1]
        if row1-1 >= 0:
            region_sum -= self.matrix[row1-1][col2]
            if col1-1 >= 0:
                region_sum += self.matrix[row1-1][col1-1]
        
        return region_sum

        

        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)