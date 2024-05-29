
def max_sum_of_A(N, B):
    A = [B[0]]
    for i in range(1, len(B)):
        A.append(max(A[i-1], B[i]))
    return sum(A) + B[-1]

# Read input
N = int(input())
B = list(map(int, input().split()))

# Get the maximum possible sum of the elements of A
result = max_sum_of_A(N, B)
print(result)
```
