class Solution:
    def findMin(self, nums: List[int]) -> int:

        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1 
        
        return nums[low]
        