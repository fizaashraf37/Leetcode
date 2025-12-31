class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = []
        ans = []

        for end in range(len(nums)):
            if len(max_heap) < k:
                heappush(max_heap, [-nums[end], end])
                continue
            ans.append(-max_heap[0][0])
            while max_heap and max_heap[0][1] <= end - k:
                heappop(max_heap)
            heappush(max_heap, [-nums[end], end])
        
        ans.append(-max_heap[0][0])
        
        return ans
            
        