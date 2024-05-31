
def is_valid(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(bracket)
    
    if len(stack) <= 1:
        return "possible"
    
    if stack[0] == stack[-1]:
        return "possible"
    
    return "impossible"

brackets = input().strip()
print(is_valid(brackets))
