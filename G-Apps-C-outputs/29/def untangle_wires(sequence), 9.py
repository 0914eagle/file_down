
def untangle_wires(sequence):
    stack = []
    
    for char in sequence:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        return "Yes"
    else:
        return "No"

# Test cases
print(untangle_wires("-+++"))  # Output: Yes
print(untangle_wires("+-"))    # Output: No
print(untangle_wires("++"))    # Output: Yes
print(untangle_wires("-"))     # Output: No
