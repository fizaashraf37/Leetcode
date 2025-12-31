class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hash_map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in "({[":
                stack.append(char)
                continue
            if not stack or stack.pop() != hash_map[char]:
                return False
        
        return not stack
        