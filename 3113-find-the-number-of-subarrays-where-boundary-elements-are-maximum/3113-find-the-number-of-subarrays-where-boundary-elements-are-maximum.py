class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:

        stack = []
        count = 0

        for i in range(len(nums)+1):
            num = nums[i] if i < len(nums) else float("inf")
            n = 1
            last_element = -1
            while stack and stack[-1] < num:
                if stack[-1] == last_element:
                    n += 1
                else:
                    n = 1
                last_element = stack.pop()
                count += n
            stack.append(num)
        
        return count
        


        # 1,4,3,2,3,2,3,1,3,4,1,2,4

        # 4,3,2,1

        # 4+3+2+1
        #  n*(n+1)/2
        