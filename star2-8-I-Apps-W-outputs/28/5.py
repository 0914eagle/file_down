
n, l, x, y = map(int, input().split())
a = list(map(int, input().split()))

marks = set(a)

if x in marks and y in marks:
    print(0)
else:
    if x not in marks:
        marks.add(x)
    if y not in marks:
        marks.add(y)
    
    print(len(marks) - len(a))
    print(*sorted(marks))

