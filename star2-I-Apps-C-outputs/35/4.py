
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

def find_pos(x):
    for i in range(n):
        if a[i] == x:
            return i
    for i in range(n):
        if b[i] == x:
            return i + n

def find_empty():
    for i in range(n):
        if a[i] == 0:
            return i
    for i in range(n):
        if b[i] == 0:
            return i + n

ans = 0
for i in range(1, n+1):
    pos = find_pos(i)
    if pos < n:
        ans += n - pos - 1
    else:
        ans += n - (pos - n) + 1
    empty = find_empty()
    a[empty] = i
    if empty >= n:
        b[empty-n] = 0

print(ans)

