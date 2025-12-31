class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calculate(operator: str, b: int, a: int) -> int:
            operations = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: int(a / b)
            }

            return operations[operator](a, b)
        
        stack = []

        for token in tokens:
            if token in "+-*/":
                stack.append(calculate(token, stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        
        return stack.pop()

        