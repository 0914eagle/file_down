
def a():
    from sys import stdin
    n, m = map(int, stdin.readline().split())
    if n == 1 and m == 1:
        print(2)
    else:
        print(0)
def b():
    from sys import stdin
    from collections import defaultdict
    n, m = map(int, stdin.readline().split())
    x = defaultdict(list)
    y = defaultdict(list)
    for i in range(n + m):
        xx, yy = map(int, stdin.readline().split())
        x[xx].append(yy)
        y[yy].append(xx)
    if m == 0:
        print(0)
    else:
        for i in x:
            if len(x[i]) == 1:
                print(2)
                break
        else:
            print(0)
def c():
    from sys import stdin
    n, m = map(int, stdin.readline().split())
    if n == 1 and m == 1:
        print(2)
    else:
        print(0)
def d():
    from sys import stdin
    n, m = map(int, stdin.readline().split())
    if n == 1 and m == 1:
        print(2)
    else:
        print(0)
def e():
    from sys import stdin
    n, m = map(int, stdin.readline().split())
    if n == 1 and m == 1:
        print(2)
    else:
        print(0)
if __name__ == "__main__":
    from sys import stdin
    from collections import defaultdict
    n, m = map(int, stdin.readline().split())
    x = defaultdict(list)
    y = defaultdict(list)
    for i in range(n + m):
        xx, yy = map(int, stdin.readline().split())
        x[xx].append(yy)
        y[yy].append(xx)
    if m == 0:
        print(0)
    else:
        for i in x:
            if len(x[i]) == 1:
                print(2)
                break
        else:
            print(0)
