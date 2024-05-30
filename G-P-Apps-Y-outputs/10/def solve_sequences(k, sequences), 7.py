
def solve_sequences(k, sequences):
    # Create a dictionary to store the sums of sequences without each element
    sums = {}
    
    # Iterate over all sequences and calculate the sums without each element
    for idx, seq in enumerate(sequences, start=1):
        for i in range(len(seq)):
            s = sum(seq) - seq[i]
            if s in sums:
                # Found a matching sum, return the indices
                return "YES", sums[s], idx, i+1
            sums[s] = idx, i+1
    
    return "NO"


# Read input
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Call the function and print the result
result = solve_sequences(k, sequences)
for line in result:
    print(line)
```
