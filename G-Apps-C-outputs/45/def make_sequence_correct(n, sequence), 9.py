
def make_sequence_correct(n, sequence):
    opening_count, closing_count = 0, 0
    unpaired_opening_count = 0
    nanoseconds = 0

    for i in range(n):
        if sequence[i] == '(':
            opening_count += 1
        else:
            closing_count += 1

        if closing_count > opening_count:
            unpaired_opening_count += closing_count - opening_count
            closing_count = opening_count

    if opening_count != closing_count:
        return -1

    nanoseconds = unpaired_opening_count + (opening_count // 2)
    return nanoseconds

# Input parsing
n = int(input())
sequence = input().strip()

result = make_sequence_correct(n, sequence)
print(result)
