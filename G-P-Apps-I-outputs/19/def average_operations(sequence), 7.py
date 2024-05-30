
def average_operations(sequence):
    total_operations = 0
    total_sequences = 0
    question_marks = sequence.count('?')

    def backtrack(sequence, operations):
        nonlocal total_operations, total_sequences

        if '?' not in sequence:
            total_operations += operations
            total_sequences += 1
            return

        idx = sequence.index('?')
        for char in ['H', 'T']:
            new_sequence = sequence[:idx] + char + sequence[idx+1:]
            if char == 'H':
                backtrack(new_sequence, operations + 1)
            else:
                backtrack(new_sequence, operations)

    backtrack(sequence, 0)
    return total_operations / total_sequences

# Input
sequence = input().strip()

# Output
result = average_operations(sequence)
print(result)
```
