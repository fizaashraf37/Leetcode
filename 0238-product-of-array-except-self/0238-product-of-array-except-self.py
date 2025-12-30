class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [1]*n

        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        
        postfix_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= postfix_product
            postfix_product *= nums[i]

        return ans




        