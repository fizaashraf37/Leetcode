class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        rightmost_indices = [len(heights)]*len(heights)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                rightmost_indices[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        stack = []
        leftmost_indices = [0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]:
                leftmost_indices[stack[-1]] = i+1
                stack.pop()
            stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            left_width = i-leftmost_indices[i]
            right_width = rightmost_indices[i] - i
            max_area = max(max_area, (left_width+right_width)*heights[i])

        return max_area


        