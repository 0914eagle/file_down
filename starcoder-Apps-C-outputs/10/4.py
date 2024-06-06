
# 120ms
# 50.00%
class Employee:
    def __init__(self, id, salary, height):
        self.id = id
        self.salary = salary
        self.height = height
        self.subordinate = []

n, m = map(int, input().split())
employees = []
for _ in range(n):
    x, y, z = map(int, input().split())
    employees.append(Employee(x, y, z))

employees.sort(key=lambda x: x.height, reverse=True)
employees.sort(key=lambda x: x.salary)

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if employees[j].salary < employees[i].salary and employees[j].height >= employees[i].height:
            employees[j].subordinate.append(employees[i])
            break

for _ in range(m):
    boss = 0
    subordinate = 0
    x = int(input())
    for employee in employees:
        if employee.id == x:
            for sub in employee.subordinate:
                subordinate += len(sub.subordinate) + 1
            boss = employee.salary
    print(boss, subordinate)
