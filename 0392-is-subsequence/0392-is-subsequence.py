class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = j = 0
        matched = 0

        for i in range(len(s)):
            while j < len(t) and s[i] != t[j]:
                j += 1
            if j < len(t) and s[i] == t[j]:
                j += 1
                matched += 1
            if j >= len(t):
                break
        
        return matched == len(s)

        