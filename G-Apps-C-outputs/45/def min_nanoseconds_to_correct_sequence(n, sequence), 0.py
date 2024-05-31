
def min_nanoseconds_to_correct_sequence(n, sequence):
    opens = 0
    closes = 0
    unbalanced = 0
    nanoseconds = 0
    
    for char in sequence:
        if char == '(':
            opens += 1
            unbalanced = opens - closes
        else:
            closes += 1
            unbalanced = opens - closes
        
        if unbalanced < 0:
            return -1
        else:
            nanoseconds += abs(unbalanced)
    
    if opens != closes:
        return -1
    else:
        return nanoseconds

# Reading input
n = int(input())
sequence = input().strip()

# Call the function and print the result
print(min_nanoseconds_to_correct_sequence(n, sequence))
