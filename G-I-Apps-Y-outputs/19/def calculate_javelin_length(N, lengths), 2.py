
def calculate_javelin_length(N, lengths):
    sum_lengths = sum(lengths)
    return sum_lengths - (N - 1)

# Input parsing
N = int(input())
lengths = []
for _ in range(N):
    lengths.append(int(input()))

# Calculate and print the length of the jumbo javelin
print(calculate_javelin_length(N, lengths))
