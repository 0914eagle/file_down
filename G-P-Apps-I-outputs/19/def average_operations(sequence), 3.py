
def average_operations(sequence):
    total_operations = 0
    total_possible_states = 0
    
    def dfs(sequence, idx, num_h, total_ops):
        nonlocal total_operations, total_possible_states
        
        if idx == len(sequence):
            total_operations += total_ops
            total_possible_states += 1
            return
        
        if sequence[idx] == 'H':
            dfs(sequence, idx + 1, num_h + 1, total_ops + num_h + 1)
        elif sequence[idx] == 'T':
            dfs(sequence, idx + 1, num_h, total_ops)
        else:
            dfs(sequence, idx + 1, num_h, total_ops)
            dfs(sequence, idx + 1, num_h + 1, total_ops + num_h + 1)
    
    dfs(sequence, 0, 0, 0)
    
    return total_operations / total_possible_states

# Input
sequence = input().strip()

# Output
print(average_operations(sequence))
```
