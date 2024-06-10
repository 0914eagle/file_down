
import sys

def get_boss_subordinates(employees, queries):
    employees.sort(key=lambda x: x[1]) # Sort employees by salary
    bosses = [None] * len(employees) # List to store boss for each employee
    for i in range(len(employees) - 1):
        for j in range(i + 1, len(employees)):
            if employees[j][2] >= employees[i][2]: # Check if employee j is eligible to be boss of employee i
                bosses[i] = employees[j][0] # Assign boss to employee i
                break

    subordinates = [0] * len(employees) # List to store number of subordinates for each employee
    for i in range(len(employees)):
        if bosses[i] is not None:
            boss_index = employees.index(bosses[i])
            subordinates[boss_index] += 1 # Increment number of subordinates for boss

    results = []
    for query in queries:
        query_index = employees.index(query)
        results.append((bosses[query_index], subordinates[query_index]))

    return results

def main():
    m, q = map(int, sys.stdin.readline().split())
    employees = []
    for _ in range(m):
        employees.append(tuple(map(int, sys.stdin.readline().split())))
    queries = []
    for _ in range(q):
        queries.append(int(sys.stdin.readline()))
    results = get_boss_subordinates(employees, queries)
    for boss, subordinates in results:
        print(boss, subordinates)

if __name__ == "__main__":
    main()

