
def solve(l, r):
    for i in range(l, r+1):
        if len(set(str(i))) == len(str(i)):
            return i
    return -1

l, r = map(int, input().split())
print(solve(l, r))