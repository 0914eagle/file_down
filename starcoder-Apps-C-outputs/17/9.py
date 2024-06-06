
from datetime import datetime, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

n, m = map(int, input().split())
lines = [list(map(int, input().split())) for i in range(n)]
days = []

for line in lines:
    days.append([line[0], line[1], line[2], line[3]])

start_date = date(2000, days[0][0], days[0][1])
end_date = date(2000, days[0][2], days[0][3])

events = {}
for single_date in daterange(start_date, end_date):
    for i in range(m):
        if i in events:
            events[i] += lines[i][4+i]
        else:
            events[i] = lines[i][4+i]

flag = False
ans = []
for i in range(m):
    try:
        ans.append(events[i]/lines[0][4+i])
        flag = True
    except ZeroDivisionError:
        flag = False
        print(-1)
        break

if flag:
    print(*[int(i) for i in ans])
