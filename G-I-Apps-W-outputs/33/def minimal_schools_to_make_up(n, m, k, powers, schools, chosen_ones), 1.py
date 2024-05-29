
def minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    chosen_powers = {student_id: powers[student_id-1] for student_id in chosen_ones}
    school_powers = {}
    
    for i in range(n):
        if schools[i] not in school_powers or powers[i] > school_powers[schools[i]]:
            school_powers[schools[i]] = powers[i]
    
    min_schools_to_make_up = 0
    sorted_chosen_powers = sorted(chosen_powers.values(), reverse=True)
    
    for power in sorted_chosen_powers:
        if all(power <= value for value in school_powers.values()):
            break
        else:
            min_schools_to_make_up += 1
    
    return min_schools_to_make_up

# Input
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Output
print(minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones))
```
