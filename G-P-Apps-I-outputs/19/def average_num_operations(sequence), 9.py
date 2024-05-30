
def average_num_operations(sequence):
    total_H = sequence.count('H')
    total_T = sequence.count('T')
    total_unknown = sequence.count('?')

    avg_operations = 0
    if total_unknown == 0:
        avg_operations = total_H
    else:
        avg_operations = total_H + (total_unknown / 2)

    return avg_operations

# Input
sequence = input().strip()

# Output
result = average_num_operations(sequence)
print(result)
```
