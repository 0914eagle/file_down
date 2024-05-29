
def fuse_javelins(N, rod_lengths):
    total_length = sum(rod_lengths)
    return total_length - (N - 1)

# Input reading
N = int(input())
rod_lengths = [int(input()) for _ in range(N)]

# Call the function and print the output
output = fuse_javelins(N, rod_lengths)
print(output)
```

