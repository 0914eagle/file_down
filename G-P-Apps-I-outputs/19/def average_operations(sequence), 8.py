
def average_operations(sequence):
    total_operations = 0
    num_unknown = sequence.count('?')
    
    for i in range(2**num_unknown):
        seq = list(sequence)
        binary_rep = bin(i)[2:].zfill(num_unknown)
        
        index = 0
        for j in range(len(seq)):
            if seq[j] == '?':
                seq[j] = binary_rep[index]
                index += 1
        
        total_operations += calculate_operations(seq)
    
    return total_operations / (2**num_unknown)

def calculate_operations(sequence):
    operations = 0
    while 'H' in sequence:
        operations += 1
        k = 0
        for i in range(len(sequence)):
            if sequence[i] == 'H':
                k += 1
            else:
                break
        for i in range(k):
            if sequence[i] == 'H':
                sequence[i] = 'T'
            else:
                sequence[i] = 'H'
    
    return operations

# Input
sequence = input().strip()

# Output
result = average_operations(sequence)
print(result)
```
