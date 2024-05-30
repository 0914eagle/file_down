
MOD = 10**9 + 7

def count_valid_evolution_plans(n, m, gyms):
    count = [0] * m
    for gym in gyms:
        for pokemon_type in gym[1:]:
            count[pokemon_type - 1] += 1

    total_pokemons = sum(count)
    ans = 1
    for i in range(total_pokemons, total_pokemons - m, -1):
        ans = (ans * i) % MOD

    for gym in gyms:
        gym_count = [0] * m
        for pokemon_type in gym[1:]:
            gym_count[pokemon_type - 1] += 1
        for i in range(m):
            for j in range(1, gym_count[i] + 1):
                ans = (ans * pow(j, MOD - 2, MOD)) % MOD

    return ans

# Input parsing
n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gym = list(map(int, input().split()))[1:]
    gyms.append(gym)

# Output
print(count_valid_evolution_plans(n, m, gyms))
```
