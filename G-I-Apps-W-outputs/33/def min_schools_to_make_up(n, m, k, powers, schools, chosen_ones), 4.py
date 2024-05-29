
def min_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    powers_dict = {}
    for i in range(n):
        if schools[i] not in powers_dict or powers[i] > powers_dict[schools[i]]:
            powers_dict[schools[i]] = powers[i]
    
    chosen_powers = [powers[i-1] for i in chosen_ones]
    chosen_powers.sort(reverse=True)
    
    min_schools = 0
    for i in range(k):
        if chosen_powers[i] < powers_dict[schools[chosen_ones[i]-1]]:
            min_schools += 1
    
    return min_schools

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Function call and output
print(min_schools_to_make_up(n, m, k, powers, schools, chosen_ones))
```
