
def length_of_javelin(N, lengths):
    total_length = sum(lengths) - (N - 1)
    return total_length

# Input parsing
N = int(input())
lengths = [int(input()) for _ in range(N)]

# Calculate and output the length of the jumbo javelin
result = length_of_javelin(N, lengths)
print(result)
```
