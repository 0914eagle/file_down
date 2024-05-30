
def calculate_average_operations(sequence):
    total_operations = 0
    total_possible_states = 0
    total_unknown_coins = sequence.count('?')

    for i in range(2 ** total_unknown_coins):
        binary_rep = bin(i)[2:].zfill(total_unknown_coins)
        possible_state = sequence.replace('?', '{}').format(*binary_rep)
        
        operations = 0
        while 'H' in possible_state:
            operations += 1
            k = possible_state.index('H') + 1
            possible_state = possible_state[:k][::-1].replace('H', 't', 1) + possible_state[k:]
        
        total_operations += operations
        total_possible_states += 1
    
    return total_operations / total_possible_states

# Read input
sequence = input().strip()

# Calculate and print the average number of operations
result = calculate_average_operations(sequence)
print(result)
```
