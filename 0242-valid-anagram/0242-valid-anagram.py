class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map = Counter(s)

        for char in t:
            if char not in hash_map:
                return False
            hash_map[char] -= 1
            if hash_map[char] == 0:
                hash_map.pop(char)
        
        return len(hash_map) == 0
        