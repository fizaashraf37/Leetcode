class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        k_smallest_sum = k_largest_sum = 0

        for i in range(k):
            k_smallest_sum += nums[i]
            k_largest_sum += nums[~i]

        return k_largest_sum - k_smallest_sum
        