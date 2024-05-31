
def can_untangle_wires(sequence):
    stack = []
    
    for char in sequence:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "Yes" if not stack else "No"

# Read input
sequence = input().strip()

# Check if wires can be untangled
result = can_untangle_wires(sequence)
print(result)
