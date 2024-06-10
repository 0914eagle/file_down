
Q = int(input())
f = lambda x: 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a, b = q[1], q[2]
        f = lambda x: f(x) + abs(x - a) + b
    else:
        print(min(range(-10**9, 10**9), key=f), f(min(range(-10**9, 10**9), key=f)))

