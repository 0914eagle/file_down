
def min_nanoseconds_to_correct_sequence(n, sequence):
    opening_count = 0
    unbalanced_count = 0
    nanoseconds = 0

    for i in range(n):
        if sequence[i] == "(":
            opening_count += 1
        else:
            if opening_count == 0:
                unbalanced_count += 1
            else:
                opening_count -= 1

    if (opening_count + unbalanced_count) % 2 != 0:
        return -1

    nanoseconds += unbalanced_count // 2
    nanoseconds += opening_count + unbalanced_count - unbalanced_count // 2

    return nanoseconds

# Input parsing
n = int(input())
sequence = input().strip()

# Call the function and print the result
print(min_nanoseconds_to_correct_sequence(n, sequence))
