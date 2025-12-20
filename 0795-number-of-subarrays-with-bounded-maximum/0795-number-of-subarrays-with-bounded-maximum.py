class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        stack = []
        nums.append(float("inf"))
        subarrays_count = 0

        for i in range(len(nums)):
            smaller_elements_count = 1
            while stack and nums[stack[-1][1]] <= nums[i]:
                smaller_elements_before = stack[-1][0]
                smaller_elements_after = i - stack[-1][1]
                if nums[stack.pop()[1]] >= left:
                    subarrays_count += smaller_elements_before * smaller_elements_after
                smaller_elements_count += smaller_elements_before
            if nums[i] <= right:
                stack.append([smaller_elements_count, i])
            
        return subarrays_count

        3,2,9,3,2,5,4,3,6,5,4,6,6,3,1,1,10,6
        5,4,3