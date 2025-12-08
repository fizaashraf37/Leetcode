class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def count_ways(i: int, cur_sum: int, memo:dict={}) -> int:

            if i == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            
            if (i,cur_sum) in memo:
                return memo[(i,cur_sum)]
            
            memo[(i,cur_sum)] = count_ways(i+1, cur_sum+nums[i], memo) + count_ways(i+1, cur_sum-nums[i], memo)
            return memo[(i,cur_sum)]
        
        return count_ways(0, 0)

        