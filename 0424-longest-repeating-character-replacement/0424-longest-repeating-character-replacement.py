class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0 
        hash_map = defaultdict(int)
        max_length = 0
        frequent_char_count = 0

        for end in range(len(s)):
            hash_map[s[end]] += 1
            frequent_char_count = max(frequent_char_count, hash_map[s[end]])
            while frequent_char_count + k < end - start + 1:
                hash_map[s[start]] -= 1
                frequent_char_count = max(frequent_char_count, hash_map[s[start]])
                start += 1
            max_length = max(max_length, end - start + 1)
        
        return max_length
