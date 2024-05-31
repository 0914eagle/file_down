
def can_untangle_wires(sequence):
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
print(can_untangle_wires("-+++"))  # Output: Yes
print(can_untangle_wires("+-"))    # Output: No
print(can_untangle_wires("++"))    # Output: Yes
print(can_untangle_wires("-"))     # Output: No
