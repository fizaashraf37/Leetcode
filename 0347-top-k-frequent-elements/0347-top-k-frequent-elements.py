class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in nums_freq.items():
            buckets[count].append(num)
        
        top_k = []

        for i in range(len(nums), -1, -1):
            top_k.extend(buckets[i])
            k -= len(buckets[i])
            if k == 0:
                break
        
        return top_k






        