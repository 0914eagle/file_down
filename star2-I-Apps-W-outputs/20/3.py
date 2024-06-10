
n = int(input())
a = list(map(int, input().split()))

def check(a):
    s = set()
    for x in a:
        if x > 0:
            if x in s:
                return False
            s.add(x)
        else:
            if -x not in s:
                return False
            s.remove(-x)
    return len(s) == 0

def solve(a):
    res = []
    cur = []
    for x in a:
        cur.append(x)
        if check(cur):
            res.append(cur)
            cur = []
    if len(cur) > 0:
        return -1
    else:
        return res

res = solve(a)
if res == -1:
    print(-1)
else:
    print(len(res))
    print(' '.join(map(str, [len(x) for x in res])))

