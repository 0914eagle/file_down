
def minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    chosen_powers = [powers[i-1] for i in chosen_ones]
    schools_powers = {}
    for i in range(n):
        school = schools[i]
        power = powers[i]
        if school in schools_powers:
            schools_powers[school] = max(schools_powers[school], power)
        else:
            schools_powers[school] = power
    
    schools_powers = sorted(schools_powers.values(), reverse=True)
    chosen_powers = sorted(chosen_powers, reverse=True)
    
    additional_schools = 0
    for i in range(k):
        if chosen_powers[i] > schools_powers[i]:
            additional_schools += 1
    
    return additional_schools

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function and print the result
result = minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
```
