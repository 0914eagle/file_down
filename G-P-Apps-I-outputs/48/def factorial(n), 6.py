
MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % MOD
    return result

def count_evolution_plans(n, m, gyms):
    total_pokemons = sum([sum(gym[1:]) for gym in gyms])
    factorial_total = factorial(total_pokemons)

    type_counts = [0] * (m+1)
    for gym in gyms:
        for pokemon_type in gym[1:]:
            type_counts[pokemon_type] += 1

    valid_counts = 1
    for i in range(1, m+1):
        valid_counts = (valid_counts * factorial(type_counts[i])) % MOD

    result = (factorial_total * pow(valid_counts, MOD-2, MOD)) % MOD
    return result

# Input parsing
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gym_info = list(map(int, input().split()))
    gyms.append(gym_info)

# Call the function with input data
result = count_evolution_plans(n, m, gyms)
print(result)
```
