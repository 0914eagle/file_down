
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort()
    res = []
    for x in b:
        cnt = 0
        for y in a:
            if x == y:
                cnt += 1
                break
            elif x > y:
                x -= y
                cnt += 1
        if x == 0:
            res.append(cnt)
        else:
            res.append(-1)
    return res

for x in solve(a, b):
    print(x)

