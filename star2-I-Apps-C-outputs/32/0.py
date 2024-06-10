
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    colors = set()
    for x in a:
        for i in range(2, x+1):
            if x % i == 0:
                colors.add(i)
                break
    return len(colors)

print(solve(a))

