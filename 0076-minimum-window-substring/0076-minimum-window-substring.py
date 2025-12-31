class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hash_map = Counter(t)
        included_chars = 0
        min_window = (0, len(s))
        start = 0

        for end in range(len(s)):
            hash_map[s[end]] -= 1
            if hash_map[s[end]] >= 0:
                included_chars += 1
            while included_chars == len(t):
                min_window_length = min_window[1] - min_window[0]
                if end - start < min_window_length:
                    min_window = (start, end)
                hash_map[s[start]] += 1
                if hash_map[s[start]] > 0:
                    included_chars -= 1
                start += 1
        
        if min_window[1] == len(s):
            return ""

        return s[min_window[0]:min_window[1]+1]


        