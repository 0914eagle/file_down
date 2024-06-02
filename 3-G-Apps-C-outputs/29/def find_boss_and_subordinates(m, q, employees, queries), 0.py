
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2]))  # Sort employees by salary (descending) and height (descending)
    
    boss = employees[0][0]  # Chairperson is the employee with the highest salary and height
    boss_height = employees[0][2]
    
    subordinates = {}  # Dictionary to store subordinates for each employee
    for i in range(1, m):
        subordinates[employees[i][0]] = 0  # Initialize number of subordinates to 0 for each employee
    
    for i in range(1, m):
        for j in range(i+1, m):
            if employees[j][2] >= employees[i][2]:  # Check if employee j is at least as tall as employee i
                subordinates[employees[j][0]] += 1  # Increment number of subordinates for employee j
    
    result = []
    for query in queries:
        if query == boss:
            result.append((boss, 0))
        else:
            boss_id = None
            for employee in employees:
                if employee[0] == query:
                    boss_id = employee[0]
                    break
            result.append((boss_id, subordinates.get(query, 0)))
    
    return result

# Read input
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)]

# Call the function and print the output
output = find_boss_and_subordinates(m, q, employees, queries)
for boss_id, num_subordinates in output:
    print(f"{boss_id} {num_subordinates}")
