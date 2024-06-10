
import sys

def get_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        m, q = map(int, lines[0].split())
        employees = []
        for i in range(1, m+1):
            emp_id, salary, height = map(int, lines[i].split())
            employees.append([emp_id, salary, height])
        queries = []
        for i in range(m+1, m+q+1):
            queries.append(int(lines[i]))
        return employees, queries

def get_boss_subordinates(employees, queries):
    employees = sorted(employees, key=lambda x: (x[1], -x[2]))
    boss_subordinates = {}
    for i, emp in enumerate(employees):
        if i == 0:
            boss_subordinates[emp[0]] = [0, 0]
        else:
            for j in range(i-1, -1, -1):
                if employees[j][1] < emp[1] and employees[j][2] <= emp[2]:
                    boss_subordinates[emp[0]] = [employees[j][0], 0]
                    boss_subordinates[employees[j][0]][1] += 1
                    break
    results = []
    for query in queries:
        results.append(boss_subordinates[query])
    return results

def main():
    employees, queries = get_input(sys.argv[1])
    results = get_boss_subordinates(employees, queries)
    for result in results:
        print(result[0], result[1])

if __name__ == "__main__":
    main()

