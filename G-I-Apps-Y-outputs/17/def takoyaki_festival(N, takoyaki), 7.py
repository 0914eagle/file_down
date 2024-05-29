
def takoyaki_festival(N, takoyaki):
    total_health_points = 0
    for i in range(N):
        for j in range(i + 1, N):
            total_health_points += takoyaki[i] * takoyaki[j]
    return total_health_points

# Input parsing
N = int(input())
takoyaki = list(map(int, input().split()))

# Call the function and print the result
result = takoyaki_festival(N, takoyaki)
print(result)
```
