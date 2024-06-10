
def solve(n, a):
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n):
        graph[i].append(i + 1)
        graph[i + 1].append(i)

    for i in range(1, n):
        if a[i - 1] == a[i]:
            return "NO"
    return "\n".join(["YES"] + [" ".join(map(str, [u, v])) for u, v in zip(range(1, n), range(2, n + 1))])

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

