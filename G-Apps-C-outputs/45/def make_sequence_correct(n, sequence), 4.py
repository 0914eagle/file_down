
def make_sequence_correct(n, sequence):
    open_count, close_count = 0, 0
    swaps_needed = 0

    for char in sequence:
        if char == '(':
            open_count += 1
        else:
            if open_count == 0:
                close_count += 1
            else:
                open_count -= 1

    if open_count == 0 and close_count == 0:
        return swaps_needed
    elif open_count % 2 == 0:  # If there are even number of unmatched open brackets
        swaps_needed += open_count // 2
        return swaps_needed
    else:
        return -1

# Reading input
n = int(input())
sequence = input()

# Calling the function and printing the result
result = make_sequence_correct(n, sequence)
print(result)
