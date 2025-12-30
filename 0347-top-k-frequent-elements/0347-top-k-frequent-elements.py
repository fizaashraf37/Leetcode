class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = Counter(nums)
        sorted_items = sorted(hash_map.items(), key = lambda x: x[1], reverse=True)

        return [key for key,_ in sorted_items[:k]]


        