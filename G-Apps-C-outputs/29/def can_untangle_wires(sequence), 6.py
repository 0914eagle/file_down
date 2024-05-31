
def can_untangle_wires(sequence):
    stack = []
    
    for wire in sequence:
        if not stack or stack[-1] != wire:
            stack.append(wire)
        else:
            stack.pop()
    
    if not stack:
        return "Yes"
    else:
        return "No"

# Read input
sequence = input().strip()

# Check if wires can be untangled
result = can_untangle_wires(sequence)
print(result)
