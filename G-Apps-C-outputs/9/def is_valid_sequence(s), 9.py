
def is_valid_sequence(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

def is_possible_to_make_valid(s):
    if is_valid_sequence(s):
        return "possible"
    
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            segment = s[:i] + ''.join(['(' if x == ')' else ')' if x == '(' else x for x in s[i:j+1]]) + s[j+1:]
            if is_valid_sequence(segment):
                return "possible"
    
    return "impossible"

# Read input
bracket_sequence = input().strip()

# Check if it is possible to make the bracket sequence valid by performing at most one segment inversion
result = is_possible_to_make_valid(bracket_sequence)
print(result)
