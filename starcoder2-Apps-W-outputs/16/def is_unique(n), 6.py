
def is_unique(n):
    s = set()
    while n:
        s.add(n % 10)
        n //= 10
    return len(s) == 4

l, r = map(int, input().split())

for i in range(l, r + 1):
    if is_unique(i):
        print(i)
        break
else:
    print(-1)
