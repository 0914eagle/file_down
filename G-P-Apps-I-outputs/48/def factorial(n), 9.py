
MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % MOD
    return result

def count_evolution_plans(n, m, gyms):
    gym_pokemon_counts = [0] * m
    for gym in gyms:
        for pokemon_type in gym[1:]:
            gym_pokemon_counts[pokemon_type - 1] += 1
    
    total_pokemon = sum(gym[0] for gym in gyms)
    
    result = 1
    for count in gym_pokemon_counts:
        result = (result * factorial(count)) % MOD
    
    result = (factorial(total_pokemon) * pow(result, MOD-2, MOD)) % MOD
    
    return result

# Input parsing
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gym_info = list(map(int, input().split()))
    gyms.append(gym_info)

# Count valid evolution plans
result = count_evolution_plans(n, m, gyms)
print(result)
```
