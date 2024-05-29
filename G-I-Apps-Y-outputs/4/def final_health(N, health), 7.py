
def final_health(N, health):
    min_health = min(health)
    return min_health

N = int(input())
health = list(map(int, input().split()))

result = final_health(N, health)
print(result)
```

