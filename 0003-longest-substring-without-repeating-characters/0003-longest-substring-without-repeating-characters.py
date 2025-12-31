class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        window_chars = set()
        max_length = 0

        for end in range(len(s)):
            while s[end] in window_chars:
                window_chars.remove(s[start])
                start += 1
            window_chars.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length



        