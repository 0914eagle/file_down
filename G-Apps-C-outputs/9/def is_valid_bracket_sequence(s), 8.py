
def is_valid_bracket_sequence(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0 or stack[-1] == ')':
                stack.append(char)
            else:
                stack.pop()

    if len(stack) == 0:
        return "possible"

    if stack.count('(') == 1 and stack.count(')') == 1:
        return "possible"

    if s[0] == ')' or s[-1] == '(':
        return "possible"

    for i in range(1, len(s)-1):
        temp = list(s)
        temp[i] = ')' if temp[i] == '(' else '('
        new_seq = ''.join(temp)
        if is_valid_bracket_sequence(new_seq) == "possible":
            return "possible"

    return "impossible"

# Input
bracket_sequence = input().strip()

# Check if it is possible to make the sequence valid
result = is_valid_bracket_sequence(bracket_sequence)
print(result)
