
def min_nanoseconds_to_correct_sequence(n, sequence):
    opening_brackets = 0
    closing_brackets = 0
    unbalanced_brackets = 0
    nanoseconds = 0
    
    for char in sequence:
        if char == '(':
            opening_brackets += 1
        else:
            closing_brackets += 1
        
        if closing_brackets > opening_brackets:
            unbalanced_brackets += 1
    
    if opening_brackets != closing_brackets:
        return -1
    
    if unbalanced_brackets % 2 == 1:
        return -1
    
    unbalanced_brackets //= 2
    
    for char in sequence:
        if char == '(':
            opening_brackets -= 1
        else:
            closing_brackets -= 1
        
        if opening_brackets == 0 and closing_brackets == 0:
            break
        if opening_brackets < closing_brackets:
            nanoseconds += abs(unbalanced_brackets)
            unbalanced_brackets = 0
    
    return nanoseconds

# Read input
n = int(input())
sequence = input()

# Call the function and print the result
print(min_nanoseconds_to_correct_sequence(n, sequence))
