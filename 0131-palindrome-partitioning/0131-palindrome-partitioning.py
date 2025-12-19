class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.partitions = []
        self.generate_partitions(0, s, [])
        return self.partitions
    
    def is_palindrome(self, left: int, right: int, s: str) -> bool:

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True 

    def generate_partitions(self, index: int, s: str, partition: List[str]):
        
        if index == len(s):
            self.partitions.append(partition.copy())
            return
        
        for i in range(index, len(s)):
            if not self.is_palindrome(index, i, s):
                continue
            substring = s[index:i+1]
            partition.append(substring)
            self.generate_partitions(i+1, s, partition)
            partition.pop()

            
        