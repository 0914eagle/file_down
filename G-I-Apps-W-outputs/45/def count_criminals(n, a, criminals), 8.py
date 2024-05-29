
def count_criminals(n, a, criminals):
    total_criminals = 0
    for i in range(n):
        distance = abs(i - a + 1)  # distance from city a
        if criminals[i] == 1:
            total_criminals += 1
        
        if distance < n and criminals[i] == 1 and criminals[distance - 1] == 1:
            total_criminals -= 1

    return total_criminals

# Input
n, a = map(int, input().split())
criminals = list(map(int, input().split()))

# Output
print(count_criminals(n, a, criminals))
```
