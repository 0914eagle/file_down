
def find_matching_sequences(k, sequences):
    sequence_sums = {}
    
    for i, seq in enumerate(sequences):
        sequence_sums[i+1] = sum(seq)
    
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            for x in range(len(sequences[i-1])):
                for y in range(len(sequences[j-1])):
                    new_sum_i = sequence_sums[i] - sequences[i-1][x]
                    new_sum_j = sequence_sums[j] - sequences[j-1][y]
                    if new_sum_i + sequences[j-1][y] == new_sum_j + sequences[i-1][x]:
                        return "YES\n{} {}\n{} {}".format(i, x+1, j, y+1)

    return "NO"

# Input parsing
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Find matching sequences
result = find_matching_sequences(k, sequences)
print(result)
