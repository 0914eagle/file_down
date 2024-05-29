
def max_sum_of_A(N, B):
    total_sum = B[0]  # Initialize total sum with the first element of B
    for i in range(1, N - 1):
        total_sum += min(B[i-1], B[i])  # Add the minimum of the adjacent elements of B to the total sum
    total_sum += B[-1]  # Add the last element of B to the total sum
    return total_sum

# Read input from Standard Input
N = int(input())
B = list(map(int, input().split()))

# Call the function and print the result
print(max_sum_of_A(N, B))
```
