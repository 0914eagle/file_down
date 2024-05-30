
def find_sequences(k, sequences):
    sums = {}
    
    for i, seq in enumerate(sequences, start=1):
        curr_sum = sum(seq)
        for j in range(len(seq)):
            new_sum = curr_sum - seq[j]
            if new_sum in sums:
                return "YES\n{} {}\n{} {}".format(sums[new_sum][0], sums[new_sum][1], i, j+1)
            
            sums[new_sum] = (i, j+1)
    
    return "NO"

# Read input
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Find and print the result
print(find_sequences(k, sequences))
```
