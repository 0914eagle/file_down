
m, q = map(int, input().split())
employees = []
for _ in range(m):
    id, salary, height = map(int, input().split())
    employees.append((id, salary, height))
employees = sorted(employees, key=lambda x: x[1])
for _ in range(q):
    id = int(input())
    idx = 0
    for i in range(m):
        if employees[i][0] == id:
            idx = i
            break
    i = idx - 1
    while i >= 0:
        if employees[i][2] >= employees[idx][2]:
            print(employees[i][0], idx - i - 1)
            break
        i -= 1
    if i < 0:
        print(0, idx)

