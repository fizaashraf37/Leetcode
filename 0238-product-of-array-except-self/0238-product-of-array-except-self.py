class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_product = [1]*n
        postfix_product = [1]*n

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1]*nums[i-1]
            postfix_product[n-i-1] = postfix_product[n-i]*nums[n-i]
        
        ans = []

        for i in range(len(nums)):
            ans.append(prefix_product[i]*postfix_product[i])

        return ans




        