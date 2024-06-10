
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
def color(a):
    s = set(a)
    if len(s) < k:
        print("NO")
    else:
        print("YES")
        for x in a:
            print(1 if x not in s else 2, end=" ")
        print()
color(a)

