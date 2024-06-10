
def solve(n, l, x, y, a):
    a.append(l)
    marks = set(a)
    for i in a:
        marks.add(i+x)
        marks.add(i+y)
    return len(a) - n, marks - set(a)
    
n, l, x, y = map(int, input().split())
a = list(map(int, input().split()))
v, p = solve(n, l, x, y, a)
print(v)
print(*p)

