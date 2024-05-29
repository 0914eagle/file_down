
def calculate_javelin_length(N, rod_lengths):
    total_length = sum(rod_lengths)
    return total_length - (N - 1)

# Reading input
N = int(input())
rod_lengths = [int(input()) for _ in range(N)]

# Calculating jumbo javelin length
javelin_length = calculate_javelin_length(N, rod_lengths)
print(javelin_length)
```
