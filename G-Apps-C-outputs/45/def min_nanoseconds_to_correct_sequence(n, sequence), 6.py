
def min_nanoseconds_to_correct_sequence(n, sequence):
    opens = 0
    unpaired_closes = 0
    nanoseconds = 0

    for char in sequence:
        if char == "(":
            opens += 1
        else:
            if opens > 0:
                opens -= 1
            else:
                unpaired_closes += 1

    nanoseconds += unpaired_closes
    unpaired_opens = opens

    if unpaired_opens >= 2:
        nanoseconds += unpaired_opens // 2
    else:
        nanoseconds = -1

    return nanoseconds

# Read input
n = int(input())
sequence = input().strip()

# Call the function and print the result
print(min_nanoseconds_to_correct_sequence(n, sequence))
