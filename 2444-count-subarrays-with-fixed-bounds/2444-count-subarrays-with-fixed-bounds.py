class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        min_queue = []
        max_queue = []
        start = 0
        subarrays_count = 0

        for i in range(len(nums)):
            if not (minK <= nums[i] <= maxK):
                start = i+1
                min_queue = []
                max_queue = []
                continue

            while min_queue and nums[min_queue[-1]] >= nums[i]:
                min_queue.pop()
            while max_queue and nums[max_queue[-1]] <= nums[i]:
                max_queue.pop()
            min_queue.append(i)
            max_queue.append(i)

            if nums[min_queue[0]] == minK and nums[max_queue[0]] == maxK:
                end = min(min_queue[0], max_queue[0])
                subarrays_count += end - start + 1
            
        return subarrays_count


        # 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
        # 8,2,3,1,4,3,5,1,5,4, 3, 5, 2, 3, 5, 1, 4, 3, 5,7,6,4,3,1,4,5,6

        1,3,5,2,7,5

        

        

        

        