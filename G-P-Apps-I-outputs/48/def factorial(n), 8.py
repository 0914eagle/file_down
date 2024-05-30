
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % (10**9 + 7)
    return result

def count_valid_evolution_plans(n, m, gyms):
    freq = [0] * (m + 1)
    for gym in gyms:
        for pokemon in gym[1:]:
            freq[pokemon] += 1

    count = 1
    for i in range(1, m + 1):
        count = (count * factorial(freq[i])) % (10**9 + 7)

    return count

# Input parsing
n, m = map(int, input().split())
gyms = [list(map(int, input().split())) for _ in range(n)]

# Output
print(count_valid_evolution_plans(n, m, gyms))
```
