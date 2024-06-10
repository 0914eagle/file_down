
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    colors = set()
    for x in a:
        for c in colors:
            if x % c == 0:
                break
        else:
            colors.add(x)
    return len(colors)

print(solve(a))

