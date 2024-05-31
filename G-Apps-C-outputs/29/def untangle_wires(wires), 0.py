
def untangle_wires(wires):
    stack = []
    
    for wire in wires:
        if stack and stack[-1] == wire:
            stack.pop()
        else:
            stack.append(wire)
    
    if not stack:
        return "Yes"
    else:
        return "No"

# Input processing
wires = input().strip()
print(untangle_wires(wires))
