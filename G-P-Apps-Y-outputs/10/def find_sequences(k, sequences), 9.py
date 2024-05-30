
def find_sequences(k, sequences):
    sequence_sums = {}
    
    for i, seq in enumerate(sequences, start=1):
        seq_sum = sum(seq)
        if seq_sum in sequence_sums:
            return "YES\n{} {}\n{} {}".format(sequence_sums[seq_sum][0], sequence_sums[seq_sum][1], i, sequence_sums[seq_sum][2])
        sequence_sums[seq_sum] = (i, -1, -1)
        
        for j, elem in enumerate(seq, start=1):
            if seq_sum - elem in sequence_sums:
                other_seq_index, other_seq_elem_index, _ = sequence_sums[seq_sum - elem]
                if i != other_seq_index:
                    return "YES\n{} {}\n{} {}".format(i, j, other_seq_index, other_seq_elem_index)
                else:
                    sequence_sums[seq_sum][1] = j
                    sequence_sums[seq_sum][2] = other_seq_elem_index
                    break

    return "NO"

# Read input
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Call the function and print the result
print(find_sequences(k, sequences))
