
def fuse_javelin_rods(N, rod_lengths):
    total_length = sum(rod_lengths) - (N - 1)
    return total_length

# Input
N = int(input())
rod_lengths = []
for _ in range(N):
    rod_length = int(input())
    rod_lengths.append(rod_length)

# Output
result = fuse_javelin_rods(N, rod_lengths)
print(result)
```
