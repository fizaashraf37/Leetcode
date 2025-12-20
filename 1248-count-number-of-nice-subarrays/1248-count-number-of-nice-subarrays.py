class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        odds_count = 0
        start = 0
        subarrays_count = 0
        evens_count_before_first_odd = 0

        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                odds_count += 1
            if odds_count > k:
                start += 1
                odds_count -= 1
                evens_count_before_first_odd = 0
            while odds_count == k and nums[start] % 2 == 0:
                evens_count_before_first_odd += 1
                start += 1
            if odds_count == k:
                subarrays_count += evens_count_before_first_odd+1
            
        return subarrays_count

        # 2,2,2,1,2,2,1,2,2,2,1,2,2,1,2
        