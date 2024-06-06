
import numpy as np
from scipy.optimize import linprog

n, m = map(int, input().split())
r = np.zeros(shape=(n, m + 2))
i = 0
while i < n:
    l = list(map(int, input().split()))
    startDay = l[0]
    startMonth = l[1]
    endDay = l[2]
    endMonth = l[3]
    if startMonth > 2:
        startMonth -= 2
    else:
        startMonth += 10
    if endMonth > 2:
        endMonth -= 2
    else:
        endMonth += 10
    start = startDay + 30 * startMonth
    end = endDay + 30 * endMonth
    for j in range(4, len(l)):
        r[i][j - 4] = l[j]
    r[i][m] = start
    r[i][m + 1] = end
    i += 1

r = r[:, 0:m + 2]
r = np.append(r, [[0 for i in range(m + 2)]], axis=0)
r[-1][-1] = 1
for i in range(m):
    r[i][i] = -365
r = r.astype(float)

b = np.zeros(shape=(n + 1, 1))
b[-1][0] = 1

result = linprog(b, A_ub=r, bounds=(None, None))
if not np.any(np.isinf(result.fun)):
    print(int(result.fun))
else:
    print(-1)
