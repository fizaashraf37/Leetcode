class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        longest_sequence_length = 0

        for num in nums:
            cur_num = num
            sequence_length = 0
            while cur_num in hash_set:
                sequence_length += 1
                hash_set.remove(cur_num)
                cur_num -= 1
            cur_num = num+1
            while cur_num in hash_set:
                sequence_length += 1
                hash_set.remove(cur_num)
                cur_num += 1
            longest_sequence_length = max(longest_sequence_length, sequence_length)
        
        return longest_sequence_length


        