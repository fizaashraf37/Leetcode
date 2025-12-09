class Solution:
    def countBits(self, n: int) -> List[int]:

        def count_set_bits(n: int) -> int:
            count = 0
            while n != 0:
                count += n & 1
                n = n >> 1
            return count
        
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = count_set_bits(i)
        
        return ans

        