class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        i = j = 0

        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    break
        
        return i == len(s)

        