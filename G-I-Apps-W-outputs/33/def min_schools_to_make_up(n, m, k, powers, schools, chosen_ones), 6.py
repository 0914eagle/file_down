
def min_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    chosen_powers = {i: powers[i-1] for i in chosen_ones}
    school_powers = {}
    for i in range(n):
        current_power = powers[i]
        current_school = schools[i]
        if current_school not in school_powers or current_power > school_powers[current_school]:
            school_powers[current_school] = current_power
    
    diff = 0
    for chosen_id, chosen_power in chosen_powers.items():
        chosen_school = schools[chosen_id - 1]
        if school_powers[chosen_school] != chosen_power:
            diff += 1
    
    return diff

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function and print the result
result = min_schools_to_make_up(n, m, k, powers, schools, chosen_ones)
print(result)
