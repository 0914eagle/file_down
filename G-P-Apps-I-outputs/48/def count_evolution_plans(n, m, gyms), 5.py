
MOD = 10**9 + 7

def count_evolution_plans(n, m, gyms):
    total_pokemons = sum([sum(types) for types in gyms])
    
    count = [0] * (m+1)
    for types in gyms:
        for t in types:
            count[t] += 1
    
    factorial = [1] * (total_pokemons+1)
    for i in range(2, total_pokemons+1):
        factorial[i] = (factorial[i-1] * i) % MOD
    
    type_count = 0
    distinct_plans = 1
    for i in range(1, m+1):
        if count[i] > 0:
            type_count += 1
            distinct_plans = (distinct_plans * factorial[count[i]]) % MOD
    
    result = (factorial[total_pokemons] * pow(distinct_plans, MOD-2, MOD)) % MOD
    return result

# Input
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    g, *types = map(int, input().split())
    gyms.append(types)

# Output
print(count_evolution_plans(n, m, gyms))
```
