
def find_min_schools(n, m, k, powers, schools, chosen_ones):
    schools_dict = {}
    for i in range(n):
        if schools[i] not in schools_dict:
            schools_dict[schools[i]] = []
        schools_dict[schools[i]].append((i+1, powers[i]))

    strongest_students = []
    for school_id, students in schools_dict.items():
        strongest_students.append(max(students, key=lambda x: x[1])[0])

    missing_chosen_ones = set(chosen_ones) - set(strongest_students)

    return max(len(missing_chosen_ones), 0)

# Input parsing
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function and output the result
result = find_min_schools(n, m, k, powers, schools, chosen_ones)
print(result)
```
