
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2], x[0]))  # Sort employees by salary (descending), height (descending), and ID (ascending)
    
    boss = employees[0][0]
    boss_height = employees[0][2]
    
    subordinates = {}
    for i in range(1, m):
        if employees[i][2] >= boss_height:
            subordinates[employees[i][0]] = boss
    
    results = []
    for query in queries:
        if query == boss:
            results.append((boss, 0))
        else:
            results.append((subordinates.get(query, boss), len([emp for emp in subordinates if subordinates[emp] == query])))
    
    return results

# Input processing
m, q = map(int, input().split())
employees = []
for _ in range(m):
    emp_id, salary, height = map(int, input().split())
    employees.append((emp_id, salary, height))

queries = []
for _ in range(q):
    queries.append(int(input()))

# Call the function and print results
results = find_boss_and_subordinates(m, q, employees, queries)
for result in results:
    print(result[0], result[1])
