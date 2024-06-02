
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2]))  # Sort employees by salary (descending) and height (descending)
    
    boss_id = employees[0][0]  # ID of the chairperson
    boss_height = employees[0][2]
    
    boss_subordinates = {boss_id: 0}  # Dictionary to store number of subordinates for each boss
    for i in range(1, m):
        boss_subordinates[employees[i][0]] = 0
    
    for i in range(1, m):
        for j in range(i-1, -1, -1):
            if employees[i][2] >= employees[j][2]:
                boss_subordinates[employees[j][0]] += 1
                break
    
    result = []
    for query in queries:
        if query == boss_id:
            result.append((boss_id, 0))
        else:
            for i in range(1, m):
                if employees[i][0] == query:
                    result.append((employees[i-1][0], boss_subordinates[query]))
                    break
    
    return result

# Read input
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)]

# Call the function and print the output
output = find_boss_and_subordinates(m, q, employees, queries)
for boss_id, num_subordinates in output:
    print(f"{boss_id} {num_subordinates}")
