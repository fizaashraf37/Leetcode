class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_freq = Counter(nums)
        min_heap = []
        top_k = [0]*k

        for num, count in nums_freq.items():
            if len(min_heap) < k:
                heappush(min_heap, [count, num])
            else:
                if count > min_heap[0][0]:
                    heappop(min_heap)
                    heappush(min_heap, [count, num])
        
        while min_heap:
            k -= 1 
            top_k[k] = heappop(min_heap)[1]
        
        return top_k






        