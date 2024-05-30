
def find_sequences(k, sequences):
    # Create a dictionary to store the sums of sequences after removing one element
    sums_dict = {}
    
    for i, seq in enumerate(sequences):
        current_sum = sum(seq)
        for j, num in enumerate(seq):
            modified_sum = current_sum - num
            if modified_sum in sums_dict:
                seq1_index = sums_dict[modified_sum]
                return "YES\n{} {}\n{} {}".format(seq1_index + 1, j + 1, i + 1, seq.index(num) + 1)
            else:
                sums_dict[modified_sum] = i
    
    return "NO"


# Read input
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Call the function and print the output
print(find_sequences(k, sequences))
