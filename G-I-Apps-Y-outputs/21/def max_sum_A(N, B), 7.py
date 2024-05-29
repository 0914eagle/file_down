
def max_sum_A(N, B):
    A = [0]*N
    A[0] = B[0]
    for i in range(1, N-1):
        A[i] = min(B[i], B[i-1])
    A[-1] = B[-1]
    return sum(A)

# Reading input
N = int(input())
B = list(map(int, input().split()))

# Calculate and output result
result = max_sum_A(N, B)
print(result)
```
