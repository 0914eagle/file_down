
def check_dishes(t, sets):
    result = []
    for _ in range(t):
        m, k = sets[_][0]
        dishes = sets[_][1]
        observations = sets[_][2:]

        remaining_dishes = dishes.copy()
        taken_dishes = set()

        for obs in observations:
            dish_index, disappointed = obs
            if dish_index != 0:
                if dish_index not in taken_dishes:
                    if disappointed:
                        remaining_dishes[dish_index - 1] -= 1
                    taken_dishes.add(dish_index)

        ans = ''
        for i in range(k):
            if sum(remaining_dishes) + len(taken_dishes) > m:
                ans += 'Y'
            else:
                ans += 'N'

        result.append(ans)

    return result


# Input parsing
t = int(input())
sets = []
for _ in range(t):
    input()  # Empty line
    m, k = map(int, input().split())
    dishes = list(map(int, input().split()))
    observations = [list(map(int, input().split())) for _ in range(m - 1)]
    sets.append([(m, k), dishes, observations])

# Call the function to check dishes availability
results = check_dishes(t, sets)

# Output results
for res in results:
    print(res)
```
