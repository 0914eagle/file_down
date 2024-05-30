
def find_sequences(k, sequences):
    sums = {}
    
    for i, seq in enumerate(sequences):
        seq_sum = sum(seq)
        if seq_sum in sums:
            return "YES\n{} {}\n{} {}".format(sums[seq_sum][0], sums[seq_sum][1], i+1, sums[seq_sum][2]+1)
        else:
            for j, num in enumerate(seq):
                new_sum = seq_sum - num
                if new_sum in sums:
                    return "YES\n{} {}\n{} {}".format(sums[new_sum][0], sums[new_sum][1]+1, i+1, j+1)
                else:
                    sums[new_sum] = (i+1, j, i)

    return "NO"

# Input
k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Output
print(find_sequences(k, sequences))
```
