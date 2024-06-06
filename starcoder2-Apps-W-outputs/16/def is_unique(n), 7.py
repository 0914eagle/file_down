
def is_unique(n):
    s = str(n)
    return len(s) == len(set(s))

l, r = map(int, input().split())

for i in range(l, r+1):
    if is_unique(i):
        print(i)
        break
else:
    print(-1)
