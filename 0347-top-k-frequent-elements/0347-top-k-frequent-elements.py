class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in nums_freq.items():
            buckets[count].append(num)
        
        top_k = []

        for i in range(len(nums), -1, -1):
            if k == 0:
                break
            for j in range(len(buckets[i])):
                top_k.append(buckets[i][j])
                k -= 1
                if k == 0:
                    break
        
        return top_k






        