
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

# Read input sequence
sequence = input().strip()

# Call the function and print the result
print(untangle_wires(sequence))
