
import sys
from itertools import combinations
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(set)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def get_independent_set(n, k):
    if k == 1:
        return set(range(1, n + 1))
    independent_set = set()
    for s in combinations(range(1, n + 1), k):
        ok = True
        for i in range(k):
            for j in range(i + 1, k):
                if s[j] in graph[s[i]]:
                    ok = False
                    break
        if ok:
            independent_set = set(s)
            break
    return independent_set


def get_cycle(n, k):
    k -= 1
    for s in combinations(range(1, n + 1), k):
        ok = True
        for i in range(k):
            for j in range(i + 1, k):
                if s[j] in graph[s[i]]:
                    ok = False
                    break
        if ok:
            cycle = list(s)
            for i in range(k - 1, 0, -1):
                cycle.append(s[i - 1])
            break
    return cycle

k = int(n ** 0.5)
if k * k < n:
    k += 1
independent_set = get_independent_set(n, k)
if len(independent_set) == k:
    print('1')
    print(len(independent_set))
    print(' '.join(map(str, independent_set)))
else:
    cycle = get_cycle(n, k)
    print('2')
    print(len(cycle))
    print(' '.join(map(str, cycle)))
