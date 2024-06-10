
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if len(stack) == 0:
                    stack = []
                else:
                    stack.pop()
                    if len(stack) == 0:
                        max_len = max(max_len, idx + 1)
                    else:
                        max_len = max(max_len, idx - stack[-1])
        
        return max_len

