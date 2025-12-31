class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        total_trapped_water = 0

        while left < right:
            cur_min_height = min(height[left], height[right])
            if height[left] < height[right]:
                trapped_water = 0
                left += 1
                while left < right and height[left] < cur_min_height:
                    trapped_water += cur_min_height - height[left]
                    left += 1
                if left <= right:
                    total_trapped_water += trapped_water
            else:
                trapped_water = 0
                right -= 1
                while left < right and height[right] < cur_min_height:
                    trapped_water += cur_min_height - height[right]
                    right -= 1
                if left <= right:
                    total_trapped_water += trapped_water
        
        return total_trapped_water
                




        