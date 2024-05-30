
MOD = 10**9 + 7

def count_valid_evolution_plans(n, m, gyms):
    total_pokemons = sum([gym[0] for gym in gyms])
    count = [0] * (m + 1)
    for gym in gyms:
        for pokemon_type in gym[1:]:
            count[pokemon_type] += 1

    ans = 1
    for i in range(1, m + 1):
        ans = ans * pow(count[i], count[i - 1], MOD) % MOD

    return ans

# Input parsing
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gym_info = list(map(int, input().split()))
    gyms.append(gym_info)

result = count_valid_evolution_plans(n, m, gyms)
print(result)
```
