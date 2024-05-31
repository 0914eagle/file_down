
def min_nanoseconds_to_correct_sequence(n, sequence):
    opening_count = 0
    move_count = 0
    for char in sequence:
        if char == '(':
            opening_count += 1
        else:
            if opening_count <= 0:
                move_count += 1
            else:
                opening_count -= 1
    
    if opening_count == 0:
        return move_count
    else:
        return -1

# Read input
n = int(input())
sequence = input().strip()

# Call the function and print the result
result = min_nanoseconds_to_correct_sequence(n, sequence)
print(result)
