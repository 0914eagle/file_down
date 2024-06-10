
def f(x):
    return abs(x - a) + b

Q = int(input())
for _ in range(Q):
    t, *ab = map(int, input().split())
    if t == 1:
        a, b = ab
    else:
        x = min(a, b)
        print(x, f(x))


S = input()
T = input()

print(T.count(S))

