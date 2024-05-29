
def min_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    school_powers = {}
    for i in range(1, m+1):
        school_powers[i] = float('-inf')
    
    for i in range(n):
        school_powers[schools[i]] = max(school_powers[schools[i]], powers[i])
    
    chosen_powers = [powers[c-1] for c in chosen_ones]
    chosen_powers.sort(reverse=True)
    
    missing_chosen_ones = chosen_powers[k-1]
    
    missing_schools = 0
    for school_power in school_powers.values():
        if school_power < missing_chosen_ones:
            missing_schools += 1
    
    return missing_schools

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function
result = min_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
```
