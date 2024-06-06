
n, m, k = map(int, input().split())
print(sum([i + 1 for i in range(k)]))
for _ in range(k):
    if _ % 2 == 0:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                print(f"({i},{j})", end=" ")
    else:
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                print(f"({i},{j})", end=" ")
    print()
