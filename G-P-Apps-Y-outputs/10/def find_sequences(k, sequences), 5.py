
def find_sequences(k, sequences):
    sums = {}
    
    for i, seq in enumerate(sequences, start=1):
        seq_sum = sum(seq)
        if seq_sum in sums:
            return "YES\n{} {}\n{} {}".format(sums[seq_sum], sequences[sums[seq_sum]].index(seq_sum) + 1, i, seq.index(seq_sum) + 1)
        else:
            for num in seq:
                if seq_sum - num in sums:
                    return "YES\n{} {}\n{} {}".format(sums[seq_sum - num], sequences[sums[seq_sum - num]].index(seq_sum - num) + 1, i, seq.index(num) + 1)
            sums[seq_sum] = i
    
    return "NO"

# Input parsing
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Call the function with the input data
result = find_sequences(k, sequences)
print(result)
