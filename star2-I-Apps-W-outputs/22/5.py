
def longestValidParentheses(s):
    stack = []
    max_len = 0
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if not stack:
                    max_len = max(max_len, i + 1)
                else:
                    max_len = max(max_len, i - stack[-1])
            else:
                stack = []
    
    return max_len

