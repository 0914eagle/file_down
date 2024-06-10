
from operator import itemgetter

def getBossSubordinates(employee, employees):
boss = None
subordinates = []
for employee_ in employees:
if employee_[1] < employee[1] and employee_[2] <= employee[2]:
if boss is None or employee_[1] < boss[1]:
boss = employee_
if employee_[1] > employee[1] and employee_[2] >= employee[2]:
subordinates.append(employee_)
return boss, subordinates

def getBossSubordinatesID(employee_id, employees):
employee = employees[employee_id]
boss, subordinates = getBossSubordinates(employee, employees)
if boss is not None:
boss_id = boss[0]
else:
boss_id = 0
return boss_id, len(subordinates)

def parseInput():
m, q = list(map(int, input().split()))
employees = {}
for _ in range(m):
employee_id, salary, height = list(map(int, input().split()))
employees[employee_id] = [employee_id, salary, height]
queries = []
for _ in range(q):
employee_id = int(input())
queries.append(employee_id)
return employees, queries

def solve():
employees, queries = parseInput()
for query in queries:
boss_id, subordinates = getBossSubordinatesID(query, employees)
print('{} {}'.format(boss_id, subordinates))

solve()

