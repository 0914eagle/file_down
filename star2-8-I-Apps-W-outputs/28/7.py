
n, l, x, y = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]

def find_mark(a, l):
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] == l:
            return a[i] + l // 2
    return -1

def find_mark_in_range(a, l, x, y):
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] >= x and a[i + 1] - a[i] <= y:
            return a[i] + (a[i + 1] - a[i]) // 2
    return -1

m1 = find_mark(a, x)
if m1 != -1:
    print(0)
else:
    m2 = find_mark_in_range(a, l, x, y)
    if m2 != -1:
        print(1)
        print(m2)
    else:
        print(2)
        print(x, y)

