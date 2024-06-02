
def find_boss_and_subordinates(m, q, employees, queries):
    employees.sort(key=lambda x: (-x[1], -x[2]))  # Sort employees by salary (descending) and height (descending)
    
    boss = employees[0][0]  # Chairperson is the employee with highest salary and tallest height
    boss_height = employees[0][2]
    
    subordinate_count = {employee[0]: 0 for employee in employees}
    
    for i in range(1, m):
        if employees[i][2] >= boss_height:
            subordinate_count[employees[i][0]] += 1
            subordinate_count[boss] += 1
    
    result = {}
    for query in queries:
        boss_id = boss
        if query != boss:
            for i in range(1, m):
                if employees[i][0] == query:
                    boss_id = employees[i-1][0]
                    break
        
        result[query] = (boss_id, subordinate_count[query])
    
    return result

# Input processing
m, q = map(int, input().split())
employees = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)]

# Call the function and print the output
output = find_boss_and_subordinates(m, q, employees, queries)
for query in queries:
    print(output[query][0], output[query][1])
