
def average_operations(sequence):
    total_operations = 0
    total_possible_states = 0

    def calculate_operations(state, index, operations):
        nonlocal total_operations, total_possible_states

        if index == len(state):
            total_operations += operations
            total_possible_states += 1
            return

        if state[index] == 'H':
            calculate_operations(state[:index] + 'T' + state[index+1:], index+1, operations+1)
        elif state[index] == 'T':
            calculate_operations(state, index+1, operations)
        else:
            calculate_operations(state[:index] + 'H' + state[index+1:], index+1, operations+1)
            calculate_operations(state[:index] + 'T' + state[index+1:], index+1, operations)

    calculate_operations(sequence, 0, 0)

    return total_operations / total_possible_states

# Input
sequence = input().strip()

# Output
print(average_operations(sequence))
```
