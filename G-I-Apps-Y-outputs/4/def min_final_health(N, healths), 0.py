
def min_final_health(N, healths):
    sorted_healths = sorted(healths)
    min_final = sorted_healths[0]
    return min_final

N = int(input())
healths = list(map(int, input().split()))

result = min_final_health(N, healths)
print(result)
```
