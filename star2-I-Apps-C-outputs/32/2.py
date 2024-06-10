
n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(a):
    colors = {}
    for x in a:
        for color in colors:
            if x % color == 0:
                colors[color] = lcm(colors[color], x)
                break
        else:
            colors[x] = x
    return len(colors)

print(solve(a))

