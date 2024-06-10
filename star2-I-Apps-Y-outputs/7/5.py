
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort()
    res = []
    for x in b:
        cnt = 0
        for coin in a:
            if coin == x:
                res.append(1)
                break
            elif coin < x:
                x -= coin
                cnt += 1
            else:
                res.append(-1)
                break
    return res

res = solve(a, b)
for x in res:
    print(x)

