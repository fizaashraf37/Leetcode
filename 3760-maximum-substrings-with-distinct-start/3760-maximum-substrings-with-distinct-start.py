class Solution:
    def maxDistinct(self, s: str) -> int:

        hash_set = set()
        count = 0

        for char in s:
            if char not in hash_set:
                hash_set.add(char)
                count += 1

        return count
        