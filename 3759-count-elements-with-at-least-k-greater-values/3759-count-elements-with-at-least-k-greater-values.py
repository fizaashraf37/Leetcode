class Solution:
    def countElements(self, nums: List[int], k: int) -> int:

        if k==0:
            return len(nums)

        nums.sort(reverse=True)
        larger_elements_count = 0
        equal_elements_count = 1
        total_count = 0

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                equal_elements_count += 1
            elif nums[i-1] > nums[i]:
                larger_elements_count += equal_elements_count
                equal_elements_count = 1
            if larger_elements_count >= k:
                total_count += 1

        return total_count

        
        