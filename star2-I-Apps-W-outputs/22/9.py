
def longestValidParentheses(s):
    stack = []
    max_len = 0
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if not stack:
                continue
            start = stack.pop()
            max_len = max(max_len, i - start + 1)
    
    return max_len

