
def catch_criminals(n, a, criminals):
    total_criminals = 0
    
    for i in range(n):
        if criminals[i] == 1:
            dist = abs(i - a + 1)
            total_criminals += 1 if dist == 1 or dist == 2 else 0
    
    return total_criminals

# Input processing
n, a = map(int, input().split())
criminals = list(map(int, input().split()))

# Call the function and print the result
print(catch_criminals(n, a - 1, criminals))
```
