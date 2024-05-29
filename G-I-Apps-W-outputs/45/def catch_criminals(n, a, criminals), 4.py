
def catch_criminals(n, a, criminals):
    caught_criminals = 0
    for i in range(n):
        dist = abs(i + 1 - a)
        if criminals[i] == 1 and (dist == 0 or criminals[a - 1 - dist] == 1 or criminals[a - 1 + dist] == 1):
            caught_criminals += 1
    return caught_criminals

# Input parsing
n, a = map(int, input().split())
criminals = list(map(int, input().split()))

# Call the function and print the result
result = catch_criminals(n, a, criminals)
print(result)
```
