
MOD = 10**9 + 7

def count_valid_evolution_plans(n, m, gyms):
    freq = [0] * (m + 1)
    sum_freq = [0] * (m + 1)
    for gym in gyms:
        for pokemon_type in gym[1:]:
            freq[pokemon_type] += 1
            sum_freq[pokemon_type] += len(gym) - 1
    
    total_pokemon = sum(sum_freq)
    result = 1
    for i in range(1, m+1):
        result = (result * pow(freq[i], sum_freq[i], MOD)) % MOD
        
    return result

# Read input
n, m = map(int, input().split())
gyms = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_valid_evolution_plans(n, m, gyms))
```
