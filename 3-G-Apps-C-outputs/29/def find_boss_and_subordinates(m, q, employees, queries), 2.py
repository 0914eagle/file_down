
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2]))  # Sort employees by salary (descending) and height (descending)
    
    boss = employees[0][0]  # Chairperson is the employee with the highest salary and tallest height
    boss_height = employees[0][2]
    
    boss_subordinates = 0
    for i in range(1, m):
        if employees[i][2] >= boss_height:
            boss_subordinates += 1
    
    results = {}
    for query in queries:
        for i in range(m):
            if employees[i][0] == query:
                boss_id = boss if i == 0 else employees[i-1][0]
                subordinates = boss_subordinates if i == 0 else 0
                results[query] = (boss_id, subordinates)
    
    return results

# Input parsing
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [input() for _ in range(q)]

# Call the function and print results
results = find_boss_and_subordinates(m, q, employees, queries)
for query in queries:
    boss_id, subordinates = results[query]
    print(f"{boss_id} {subordinates}")
