
def can_untangle_wires(sequence):
    stack = []
    
    for wire in sequence:
        if not stack or stack[-1] != wire:
            stack.append(wire)
        else:
            stack.pop()
    
    return "Yes" if not stack else "No"

# Read input
sequence = input().strip()

# Check if wires can be untangled
result = can_untangle_wires(sequence)
print(result)
