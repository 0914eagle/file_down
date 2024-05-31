
def is_wires_untangled(sequence):
    stack = []
    
    for wire in sequence:
        if not stack:
            stack.append(wire)
        else:
            if stack[-1] == wire:
                stack.pop()
            else:
                stack.append(wire)
    
    return "Yes" if not stack else "No"

# Test cases
print(is_wires_untangled("-++-"))  # Yes
print(is_wires_untangled("+-"))    # No
print(is_wires_untangled("++"))    # Yes
print(is_wires_untangled("-"))     # No
