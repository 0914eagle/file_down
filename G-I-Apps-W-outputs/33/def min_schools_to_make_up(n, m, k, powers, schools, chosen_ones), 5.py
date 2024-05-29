
def min_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
    selected_chosen_ones = []
    for c in chosen_ones:
        selected_chosen_ones.append((c, powers[c-1], schools[c-1]))
    
    selected_chosen_ones.sort(key=lambda x: x[1], reverse=True)
    
    required_schools = set()
    for student in selected_chosen_ones:
        if len(required_schools) == k:
            break
        required_schools.add(student[2])
    
    return len(required_schools)

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Output
print(min_schools_to_make_up(n, m, k, powers, schools, chosen_ones))
```
