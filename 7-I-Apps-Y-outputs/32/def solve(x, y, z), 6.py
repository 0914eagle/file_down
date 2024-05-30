

def solve(x, y, z):
    return (x-2*z)//(y+z)


x, y, z = map(int, input().split())
print(solve(x, y, z))

