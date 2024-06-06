
def solve():
    l, r = map(int, input().split())
    for i in range(l, r+1):
        if len(set(str(i))) == len(str(i)):
            print(i)
            return
    print(-1)

solve()
