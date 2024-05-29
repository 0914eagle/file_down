
def max_possible_sum_of_A(N, B):
    cumul_sum = B[0]
    for i in range(1, N-1):
        cumul_sum += min(B[i-1], B[i])
    return cumul_sum + B[-1]

# Reading input
N = int(input())
B = list(map(int, input().split()))

# Output
print(max_possible_sum_of_A(N, B))
```
