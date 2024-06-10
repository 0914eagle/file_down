
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

def check_string(s):
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or (s[i] == 'a' and s[j] == 'b') or (s[i] == 'b' and s[j] == 'c'):
                    if j + 1 not in graph[i + 1]:
                        return False
    return True

for a in range(n):
    for b in range(n):
        for c in range(n):
            if a + b + c == n:
                s = ['a'] * a + ['b'] * b + ['c'] * c
                if check_string(s):
                    print("Yes")
                    print("".join(s))
                    exit(0)

print("No")

