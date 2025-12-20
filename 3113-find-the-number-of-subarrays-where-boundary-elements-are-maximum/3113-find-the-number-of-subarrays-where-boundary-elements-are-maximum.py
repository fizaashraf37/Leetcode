class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:

        stack = []
        count = 0
        nums.append(float("inf"))

        for i in range(len(nums)):
            n = 1
            last_element = -1
            while stack and stack[-1] < nums[i]:
                if stack[-1] == last_element:
                    n += 1
                else:
                    n = 1
                last_element = stack.pop()
                count += n
            stack.append(nums[i])
        
        return count
        


        # 1,4,3,2,3,2,3,1,3,4,1,2,4

        # 4,3,2,1

        # 4+3+2+1
        #  n*(n+1)/2
        