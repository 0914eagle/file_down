
def find_sequences(k, sequences):
    sums = {}
    for i, seq in enumerate(sequences):
        s = sum(seq)
        if s in sums:
            return "YES\n{} {}\n{} {}".format(sums[s][0]+1, sums[s][1]+1, i+1, sums[s][2]+1)
        for j, num in enumerate(seq):
            if s - num in sums:
                return "YES\n{} {}\n{} {}".format(sums[s-num][0]+1, sums[s-num][1]+1, i+1, j+1)
            sums[s - num] = (i, j, j)

    return "NO"

k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

print(find_sequences(k, sequences))
```
