
def find_boss_and_subordinates(employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2], x[0]))  # Sort employees by salary, height, and ID
    boss = employees[0][0]  # Chairperson is the employee with the highest salary and height
    boss_height = employees[0][2]
    
    subordinate_count = {boss: 0}
    boss_of = {boss: 0}
    
    for i in range(1, len(employees)):
        emp_id, salary, height = employees[i]
        boss_id = None
        
        for j in range(i-1, -1, -1):
            if employees[j][2] >= height:
                boss_id = employees[j][0]
                break
        
        boss_of[emp_id] = boss_id
        subordinate_count[emp_id] = 0
        
        if boss_id is not None:
            subordinate_count[boss_id] += 1
    
    result = []
    for query in queries:
        boss_id = boss_of.get(query, 0)
        subordinates = subordinate_count.get(query, 0)
        result.append((boss_id, subordinates))
    
    return result

# Read input
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)]

# Find boss and subordinates for each query
output = find_boss_and_subordinates(employees, queries)

# Print output
for boss_id, subordinates in output:
    print(f"{boss_id} {subordinates}")
