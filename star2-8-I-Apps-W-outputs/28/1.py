
from sys import stdin, stdout

n, l, x, y = map(int, stdin.readline().split())
marks = list(map(int, stdin.readline().split()))

if x not in marks:
    marks.append(x)
if y not in marks:
    marks.append(y)

marks.sort()

v = 0
p = []
for i in range(1, len(marks)):
    if marks[i] - marks[i-1] == x or marks[i] - marks[i-1] == y:
        continue
    
    v += 1
    p.append(marks[i-1] + x)

stdout.write(f"{v}\n")
stdout.write(" ".join(map(str, p)))

