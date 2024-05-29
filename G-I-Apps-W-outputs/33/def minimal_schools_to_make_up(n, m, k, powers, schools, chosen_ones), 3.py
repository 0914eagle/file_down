
def minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    students = {}
    for i, (power, school) in enumerate(zip(powers, schools)):
        if school not in students or students[school][0] < power:
            students[school] = (power, i+1)
    
    chosen_powers = [powers[idx-1] for idx in chosen_ones]
    chosen_schools = set(schools[idx-1] for idx in chosen_ones)
    
    remaining_chosen = k - len(chosen_schools)
    
    ranked_students = sorted(students.values(), reverse=True)
    
    remaining_strongest = []
    for power, idx in ranked_students:
        if idx not in chosen_ones:
            remaining_strongest.append(power)
        if len(remaining_strongest) >= remaining_chosen:
            break
    
    min_schools_needed = 0
    for power in remaining_strongest:
        if power in chosen_powers:
            chosen_powers.remove(power)
        else:
            min_schools_needed += 1

    return min_schools_needed

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

result = minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
```
