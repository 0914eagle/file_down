
def min_nanoseconds_to_correct_sequence(n, sequence):
    opening = 0
    closing = 0
    unpaired = 0
    nanoseconds = 0
    
    for char in sequence:
        if char == '(':
            opening += 1
            if unpaired > 0:
                unpaired -= 1
            else:
                closing += 1
        else:
            closing += 1
            unpaired = closing - opening
            
    if closing != opening:
        return -1
    
    return closing // 2

# Input
n = int(input())
sequence = input().strip()

# Output
print(min_nanoseconds_to_correct_sequence(n, sequence))
