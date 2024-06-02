
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2]))  # Sort employees by salary (descending) and height (descending)
    
    boss = employees[0][0]  # Chairperson is the employee with the highest salary and tallest height
    boss_height = employees[0][2]
    
    boss_dict = {boss: []}  # Dictionary to store boss-subordinate relationships
    
    for i in range(1, m):
        emp_id, emp_salary, emp_height = employees[i]
        boss_found = False
        
        for j in range(i-1, -1, -1):
            if employees[j][2] >= emp_height:  # Check if there is a boss taller than the employee
                boss_dict[employees[j][0]].append(emp_id)
                boss_found = True
                break
        
        if not boss_found:
            boss_dict[boss].append(emp_id)
    
    result = []
    for query in queries:
        if query == boss:
            result.append((boss, 0))
        else:
            for key, value in boss_dict.items():
                if query in value:
                    result.append((key, len(value)))
                    break
    
    return result

# Input parsing
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)]

# Call the function and print the output
output = find_boss_and_subordinates(m, q, employees, queries)
for boss_id, num_subordinates in output:
    print(boss_id, num_subordinates)
