class Solution:
    
    # Time Complexity: O(4N)
    # Space Complexity: O(2N)
    def trapOld(self, height: List[int]) -> int:
        max_left_heights = [0]*len(height)
        max_right_heights = [0]*len(height)

        for i in range(1, len(height)):
            max_left_heights[i] = max(max_left_heights[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right_heights[i] = max(max_right_heights[i + 1], height[i + 1])
        for i in range(len(height)):
            max_right_heights[i] = min(max_left_heights[i], max_right_heights[i])
        max_right_heights = min(max_left_heights, max_right_heights)

        for i,h in enumerate(height):
            max_right_heights[i] = max(0, max_right_heights[i]-h)

        return sum(max_right_heights)
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def trap1(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        
        max_left_height, max_right_height = height[left], height[right]
        cur_idx = left
        total = 0
        
        while left < right:
            water_level = min(max_left_height, max_right_height)
            units = water_level - height[cur_idx]
            total += max(0, units)
            if max_left_height <= max_right_height:
                left += 1
                max_left_height = max(max_left_height, height[left])
                cur_idx = left
            else:
                right -= 1
                max_left_height = max(max_right_height, height[right])
                cur_idx = right
            
        return total
    
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def trap2(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        
        max_left, max_right = height[left], height[right]
        total = 0
        
        while left < right:
            if max_left <= max_right:
                # we do not need to take the min since max_left is already smaller than
                # max_right
                left += 1
                max_left = max(max_left, height[left])
                # here values will not go negative since max_left is greater than 
                # current height
                total += max_left-height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                total += max_right-height[right]
            
        return total
    
    def trap(self, heights: List[int]) -> int:
        
        max_left_height, max_right_height = heights[0], heights[-1]
        left, right = 0, len(heights)-1
        units = 0

        while left <= right:
            max_left_height = max(max_left_height, heights[left])
            max_right_height = max(max_right_height, heights[right])
            water_level = min(max_left_height, max_right_height)

            if max_left_height < max_right_height:
                units += water_level - heights[left]
                left += 1
            else:
                units += water_level - heights[right]
                right -= 1

        return units
    
    def trap3(self, heights: List[int]) -> int:
        
        # intuition: we can trap water in between the walls where there are gaps. and we can store water till the min height
        # of left and right walls. If the current index height is equal to the min height then we know that this is either 
        # our left wall or right wall,m and we cannot store any water above the wall as that will spill out of the wall. And
        # if the current hieght is larger than the min height, we know that this is the other wall as any water stored between
        # this wall and min height wall will spill from the min height wall. So no water can be stored in this case well. 
        # therefore we can only store water at indices where height is smaller than min height and the units of water that
        # can be stored at that index or gap is difference of min_height and cur_height
        
        left_max_height = [0]*len(heights)
        right_max_height = [0]*len(heights)
        left_max_height[0], right_max_height[-1] = heights[0], heights[-1]
        
        for i in range(1, len(heights)):
            left_max_height[i] = max(left_max_height[i-1], heights[i])
        
        for i in range(len(heights)-2, -1, -1):
            right_max_height[i] = max(right_max_height[i+1], heights[i])
        
        total_units_trapped = 0
        
        for i in range(len(heights)):
            left_max_height[i] = min(left_max_height[i], right_max_height[i])
            total_units_trapped += max(0, left_max_height[i] - heights[i])
        
        return total_units_trapped
    
    def trap(self, heights: List[int]) -> int:
        
        # we can solve this in O(1) space using two pointers. Since we need to know the min height of two walls, so
        # we can find it by comparing the leftmost and rightmost walls. If the left height becomes larger than right height
        # we know that we have found the right boundary of the walls behind the current left pointer. And we will now try
        # to find the right boundary for current left pointer or right boundary for walls behind left pointer in case this left             # pointer moves ahead. If we didn't move left pointer and instead moved right pointer and we find a wall larger
        # than right wall, then we found the left boundary for the right wall. 
        
        max_left_height, max_right_height = 0, heights[-1]
        left, right = 0, len(heights)-1
        units_trapped = 0
        
        while left <= right:
            max_left_height = max(max_left_height, heights[left])
            max_right_height = max(max_right_height, heights[right])
            min_height = min(max_left_height, max_right_height)
            
            if max_left_height < max_right_height:
                units_trapped += min_height - heights[left]
                left += 1
            else:
                units_trapped += min_height - heights[right]
                right -= 1
            
        return units_trapped
            
            
        
            
        
            
            
            
                
                
                
        