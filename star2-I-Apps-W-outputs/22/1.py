
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                max_len = max(max_len, i - 0)
            else:
                stack.pop()
                if len(stack) == 0:
                    max_len = max(max_len, i - 0)
                else:
                    max_len = max(max_len, i - stack[-1])
    return max_len

