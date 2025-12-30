class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_map = Counter(s)

        for char in t:
            if char not in hash_map or hash_map[char] == 0:
                return False
            hash_map[char] -= 1
        
        return True
        