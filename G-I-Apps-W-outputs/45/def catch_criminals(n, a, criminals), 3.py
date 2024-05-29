
def catch_criminals(n, a, criminals):
    total_criminals = 0

    for i in range(n):
        if criminals[i] == 1:
            distance = abs(a - (i + 1))
            total_criminals += criminals[i]

    return total_criminals

# Read input
n, a = map(int, input().split())
criminals = list(map(int, input().split()))

# Call the function and print the result
print(catch_criminals(n, a, criminals))
```
