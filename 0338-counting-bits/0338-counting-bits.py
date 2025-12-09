class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        ans = [0,1]
        bits_range = 2

        while len(ans) < n+1:
            for i in range(bits_range):
                ans.append(ans[i]+1)
                if len(ans) == n+1:
                    break
            bits_range = bits_range << 1
            
        return ans

        