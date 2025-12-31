class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash_map = Counter(s1)
        start = 0

        for end in range(len(s2)):
            hash_map[s2[end]] -= 1
            while hash_map[s2[end]] < 0 and start <= end:
                hash_map[s2[start]] += 1
                start += 1
            if end - start + 1 == len(s1):
                return True
        
        return False
            
        