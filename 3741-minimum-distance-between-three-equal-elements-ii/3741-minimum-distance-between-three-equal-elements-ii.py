class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        hash_map = defaultdict(list)

        for i, num in enumerate(nums):
            hash_map[num].append(i)

        min_absoulte_distance = float("inf")
        
        for num, indices in hash_map.items():
            if len(indices) < 3:
                continue
            for idx in range(0, len(indices)-2):
                i, j, k = indices[idx], indices[idx+1], indices[idx+2]
                distance = abs(i-j) + abs(j-k) + abs(k-i)
                min_absoulte_distance = min(min_absoulte_distance, distance)

        return min_absoulte_distance if min_absoulte_distance != float("inf") else -1