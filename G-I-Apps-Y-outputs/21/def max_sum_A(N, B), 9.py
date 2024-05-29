
def max_sum_A(N, B):
    max_sum = sum(B)
    max_sum += max(B[0], B[-1])
    return max_sum

# Read input
N = int(input())
B = list(map(int, input().split()))

# Call the function and print the result
print(max_sum_A(N, B))
```
