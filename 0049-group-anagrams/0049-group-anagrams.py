class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def anagram_count(s: str) -> tuple:
            char_count = {ch: 0 for ch in string.ascii_lowercase}
            for char in s:
                char_count[char] += 1
            return tuple(char_count[ch] for ch in string.ascii_lowercase)

        hash_map = {}
        ans = []

        for s in strs:
            anagram_counts = anagram_count(s)
            if anagram_counts in hash_map:
                group_id = hash_map[anagram_counts]
                ans[group_id].append(s)
            else:
                group_id = len(hash_map)
                hash_map[anagram_counts] = group_id
                ans.append([s])
        
        return ans
            
        