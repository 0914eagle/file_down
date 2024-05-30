
def solve_problem(k, sequences):
    total_sums = {}
    for i, seq in enumerate(sequences, start=1):
        total_sum = sum(seq)
        if total_sum in total_sums:
            return "YES\n{} {}\n{} {}".format(total_sums[total_sum][0], total_sums[total_sum][1], i, 1)
        else:
            for j, num in enumerate(seq, start=1):
                partial_sum = total_sum - num
                if partial_sum in total_sums:
                    return "YES\n{} {}\n{} {}".format(total_sums[partial_sum][0], total_sums[partial_sum][1], i, j)
                total_sums[partial_sum] = (i, j)
    return "NO"

# Input
k = int(input())
sequences = []
for _ in range(k):
    n_i = int(input())
    sequence = list(map(int, input().split()))
    sequences.append(sequence)

# Output
print(solve_problem(k, sequences))
```
