
def fuse_steel_rods(N, lengths):
    total_length = sum(lengths) - (N - 1)
    return total_length

# Input parsing
N = int(input().strip())
lengths = [int(input().strip()) for _ in range(N)]

# Call the function and print the output
result = fuse_steel_rods(N, lengths)
print(result)
```
