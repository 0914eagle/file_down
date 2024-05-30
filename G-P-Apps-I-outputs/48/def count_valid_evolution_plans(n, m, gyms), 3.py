
MOD = 10**9 + 7

def count_valid_evolution_plans(n, m, gyms):
    count = [0] * (m+1)
    for gym in gyms:
        for pokemon_type in gym[1:]:
            count[pokemon_type] += 1
    
    total_pokemon = sum(count[1:])
    
    result = 1
    for i in range(1, m+1):
        result *= pow(count[i], count[i]-1, MOD)
        result %= MOD

    return result

# Input
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gyms.append(list(map(int, input().split())))

# Output
print(count_valid_evolution_plans(n, m, gyms))
```
