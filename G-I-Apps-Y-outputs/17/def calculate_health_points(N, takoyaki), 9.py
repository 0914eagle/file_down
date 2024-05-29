
def calculate_health_points(N, takoyaki):
    total_hp = 0
    for i in range(N):
        for j in range(i+1, N):
            total_hp += takoyaki[i] * takoyaki[j]
    return total_hp

# Read input
N = int(input())
takoyaki = list(map(int, input().split()))

# Call the function and print the result
print(calculate_health_points(N, takoyaki))
```
