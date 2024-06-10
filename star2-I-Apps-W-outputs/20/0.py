
def solve(a):
    n = len(a)
    employees = set()
    for i in range(n):
        if a[i] > 0:
            if a[i] in employees:
                return -1
            employees.add(a[i])
        else:
            if -a[i] not in employees:
                return -1
            employees.remove(-a[i])
    days = []
    day = []
    for i in range(n):
        if a[i] > 0:
            day.append(a[i])
        else:
            day.append(a[i])
            days.append(day)
            day = []
    if len(day) > 0:
        days.append(day)
    return len(days), [len(day) for day in days]

n = int(input())
a = list(map(int, input().split()))
result = solve(a)
if result == -1:
    print(result)
else:
    d, c = result
    print(d)
    print(' '.join(map(str, c)))

