
def max_sum_of_A(N, B):
    max_sum = sum(B)
    for i in range(N-2):
        max_sum += min(B[i], B[i+1])
    return max_sum

# Read input
N = int(input())
B = list(map(int, input().split()))

# Call the function and print the output
print(max_sum_of_A(N, B))
```
