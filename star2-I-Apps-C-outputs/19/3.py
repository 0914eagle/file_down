
import sys

def solve(n, C, p, b, u):
    users = [(p[i], b[i], u[i], i) for i in range(n)]
    users.sort()
    total_uploaded = 0
    min_buffer = float('inf')
    for i in range(n):
        user_p, user_b, user_u, user_i = users[i]
        buffer_size = user_b - (user_p + C)
        min_buffer = min(min_buffer, buffer_size)
        total_uploaded += user_u
        if total_uploaded >= user_b:
            break
    return min_buffer

n, C = map(int, sys.stdin.readline().split())
p = [0] * n
b = [0] * n
u = [0] * n
for i in range(n):
    p[i], b[i], u[i] = map(int, sys.stdin.readline().split())

print(solve(n, C, p, b, u))

