
def find_available_dishes(t, sets):
    results = []
    
    for i in range(t):
        m, k = sets[i][0]
        a = sets[i][1]
        observations = sets[i][2:]

        dish_count = a.copy()
        for j in range(m - 1):
            t_j, r_j = observations[j]
            if t_j != 0 and r_j == 0:
                dish_count[t_j - 1] -= 1

        result = ""
        for count in dish_count:
            if count >= m - 1:
                result += "N"
            else:
                result += "Y"
        
        results.append(result)
    
    return results


# Input parsing
t = int(input())
sets = []
for _ in range(t):
    empty_line = input()
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    observations = []
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        observations.append((t_j, r_j))
    
    sets.append([(m, k), a, observations])

# Get results
results = find_available_dishes(t, sets)

# Output results
for result in results:
    print(result)
```
