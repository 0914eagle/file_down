
def calculate_javelin_length(N, rods):
    total_length = sum(rods)
    final_length = total_length - (N - 1)
    return final_length

# Input
N = int(input())
rods = []
for _ in range(N):
    rods.append(int(input()))

# Output
print(calculate_javelin_length(N, rods))
```
