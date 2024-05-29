
def minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    schools_powers = [[] for _ in range(m+1)]
    for i, power in enumerate(powers):
        school = schools[i]
        schools_powers[school].append((power, i+1))

    schools_powers = [sorted(school, reverse=True) for school in schools_powers]

    chosen_ones_powers = [(powers[chosen-1], chosen) for chosen in chosen_ones]
    chosen_ones_powers.sort(reverse=True)

    updated_chosen_ones = []
    total_schools_made_up = 0

    for power, chosen in chosen_ones_powers:
        school = schools[chosen-1]
        position = schools_powers[school].index((power, chosen))
        
        if position == 0:
            updated_chosen_ones.append(chosen)
        else:
            total_schools_made_up += 1
            for new_school in range(1, m+2):
                if new_school != school and (len(schools_powers[new_school]) == 0 or powers[schools_powers[new_school][0][1]-1] < power):
                    schools_powers[new_school].append((power, chosen))
                    schools_powers[new_school] = sorted(schools_powers[new_school], reverse=True)
                    updated_chosen_ones.append(chosen)
                    break

    return total_schools_made_up

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

result = minimal_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
```

