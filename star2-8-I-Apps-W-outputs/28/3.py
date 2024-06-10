
n, l, x, y = map(int, input().split())
a = [0] + list(map(int, input().split())) + [l]

def check(d):
    for i in range(1, n+2):
        for j in range(i+1, n+2):
            if a[j] - a[i] == d:
                return True
    return False

if check(x) and check(y):
    print(0)
else:
    if not check(x):
        print(1)
        print(x)
    elif not check(y):
        print(1)
        print(y)
    else:
        print(2)
        print(x, y)

