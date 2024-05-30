
def calculate_average_operations(s):
    total_possible_states = 0
    total_operations = 0

    # Helper function to calculate the number of operations needed for a specific state
    def calculate_operations(state):
        operations = 0
        h_count = 0
        total_coins = len(state)

        for coin in state:
            if coin == 'H':
                h_count += 1
                operations += h_count
            elif coin == 'T':
                if h_count > 0:
                    h_count -= 1
        
        return operations
    
    # Generate all possible sequences replacing '?' with 'H' and 'T'
    for i in range(2 ** s.count('?')):
        seq = list(s)
        for j in range(len(seq)):
            if seq[j] == '?':
                seq[j] = 'H' if i & (1 << (j - seq.index('?'))) else 'T'
        
        total_possible_states += 1
        total_operations += calculate_operations(seq)
    
    return total_operations / total_possible_states

# Input sequence
input_sequence = input().strip()

# Calculate and print the average number of operations
print(calculate_average_operations(input_sequence))
```
