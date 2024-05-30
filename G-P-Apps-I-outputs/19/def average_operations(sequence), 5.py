
def average_operations(sequence):
    total_operations = 0
    total_configurations = 0
    
    def calculate_operations(current_sequence, operations):
        nonlocal total_operations, total_configurations
        
        if '?' not in current_sequence:
            total_operations += operations
            total_configurations += 1
            return
        
        idx = current_sequence.index('?')
        next_sequence = current_sequence[:idx] + 'H' + current_sequence[idx+1:]
        calculate_operations(next_sequence, operations + 1)
        
        next_sequence = current_sequence[:idx] + 'T' + current_sequence[idx+1:]
        calculate_operations(next_sequence, operations + 1)
    
    calculate_operations(sequence, 0)
    
    return total_operations / total_configurations

# Input
sequence = input().strip()

# Output
print(average_operations(sequence))
```
