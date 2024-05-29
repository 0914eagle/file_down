
def max_f(n, a):
    max_val = max(a) - 1
    remainders_sum = sum(map(lambda x: max_val % x, a))
    return remainders_sum

# Read input values
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_f(n, a))
```
