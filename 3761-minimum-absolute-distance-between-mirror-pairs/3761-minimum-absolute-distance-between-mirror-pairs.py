class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        hash_map = defaultdict(list)
        reverse_nums_cache = defaultdict(int)

        for num in nums:
            if num in reverse_nums_cache:
                continue
            reversed_num = self.reverse_num(num)
            reverse_nums_cache[num] = reversed_num
            hash_map[reversed_num] = []

        for i in range(len(nums)-1,-1,-1):
            if nums[i] in hash_map:
                hash_map[nums[i]].append(i)
                
        min_absolute_diff = float("inf")
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]].pop()
            reversed_num = reverse_nums_cache[nums[i]]
            if len(hash_map[reversed_num]) > 0:
                j = hash_map[reversed_num][-1]
                min_absolute_diff = min(min_absolute_diff, abs(i-j))
                    
        return min_absolute_diff if min_absolute_diff != float("inf") else -1 
    
    def reverse_num(self, num) -> int:
        reversed_num = 0
        while num != 0:
            remainder = num%10
            num //= 10
            reversed_num = (reversed_num*10)+remainder

        return reversed_num