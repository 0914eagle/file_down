
def maximize_sum_of_A(N, B):
    A = [0] * (N+1)
    for i in range(N-1):
        if i == 0:
            A[i] = B[i]
        else:
            A[i] = min(B[i-1], B[i])
    A[N-1] = B[N-2]
    
    return sum(A)

# Taking input from Standard Input
N = int(input())
B = list(map(int, input().split()))

# Calling the function to get the maximum sum of A
result = maximize_sum_of_A(N, B)
print(result)
```
