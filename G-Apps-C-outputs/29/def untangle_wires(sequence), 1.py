
def untangle_wires(sequence):
    stack = []
    
    for char in sequence:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    
    if not stack:
        return "Yes"
    else:
        return "No"

# Example usage
sequence = "-+++"
result = untangle_wires(sequence)
print(result)
