
def minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    chosen_powers = [powers[chosen - 1] for chosen in chosen_ones]
    school_dict = {}
    for i in range(n):
        if schools[i] not in school_dict or powers[i] > school_dict[schools[i]]:
            school_dict[schools[i]] = powers[i]
    
    new_schools_needed = 0
    for power in chosen_powers:
        if all(power <= value for value in school_dict.values()):
            continue
        new_schools_needed += 1
    
    return new_schools_needed

# Input reading
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function
result = minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
```
