
def solve(x, a, b):
    if b - a <= x:
        return 'safe'
    elif b - a > x + 1:
        return 'dangerous'
    else:
        return 'delicious'

print(solve(int(input().split()[0]), int(input().split()[1]), int(input().split()[2])))

