
from collections import deque

n = int(input())
s = input()

time = 0
q = deque()
for i in range(n):
    if s[i] == 'P':
        q.append(i)

ans = 1
while q:
    i = q.popleft()
    if s[i] == '*':
        ans = time + 1
        break
    if i > 0 and s[i-1] == 'P':
        q.append(i-1)
    if i < n-1 and s[i+1] == 'P':
        q.append(i+1)
    s = s[:i] + 'P' + s[i+1:]
    time += 1

print(ans)
