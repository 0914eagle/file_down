
def find_sequences(k, sequences):
    sums = {}
    for i, seq in enumerate(sequences):
        cur_sum = sum(seq)
        if cur_sum in sums:
            return "YES\n{} {}\n{} {}".format(sums[cur_sum][0], sums[cur_sum][1], i+1, sums[cur_sum][2]+1)
        for j, num in enumerate(seq):
            if cur_sum - num in sums:
                return "YES\n{} {}\n{} {}".format(sums[cur_sum - num][0], sums[cur_sum - num][1]+1, i+1, j+1)
            sums[cur_sum - num] = (i+1, j, i)
    return "NO"

# Input
k = int(input())
sequences = []
for _ in range(k):
    n_i = int(input())
    seq = list(map(int, input().split()))
    sequences.append(seq)

# Output
print(find_sequences(k, sequences))
