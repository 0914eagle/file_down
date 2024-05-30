
MOD = 10**9 + 7

def count_valid_evolution_plans(n, m, gyms):
    # Initialize a list to keep track of the count of each Pokemon type before evolution
    count_before = [0] * m
    
    # Count the number of each Pokemon type before evolution
    for gym in gyms:
        for pokemon_type in gym[1:]:
            count_before[pokemon_type - 1] += 1
    
    # Calculate the factorial modulo MOD
    factorial_mod = [1] * (max(count_before) + 1)
    for i in range(2, len(factorial_mod)):
        factorial_mod[i] = (factorial_mod[i - 1] * i) % MOD
    
    # Initialize a list to store the count of each type of Pokemon after evolution
    count_after = [0] * m
    
    # Calculate the total number of Pokemon
    total_pokemon = sum(count_before)
    
    # Calculate the number of valid evolution plans
    result = 1
    for i in range(m):
        result = (result * factorial_mod[count_before[i]]) % MOD
    
    return result

# Input
n, m = map(int, input().split())
gyms = [list(map(int, input().split())) for _ in range(n)]

# Output
print(count_valid_evolution_plans(n, m, gyms))
```
