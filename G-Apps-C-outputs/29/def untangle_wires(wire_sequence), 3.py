
def untangle_wires(wire_sequence):
    stack = []
    
    for wire in wire_sequence:
        if not stack or stack[-1] != wire:
            stack.append(wire)
        else:
            stack.pop()
    
    if not stack:
        return "Yes"
    else:
        return "No"

# Read input
wire_sequence = input().strip()

# Call the function and print the result
print(untangle_wires(wire_sequence))
