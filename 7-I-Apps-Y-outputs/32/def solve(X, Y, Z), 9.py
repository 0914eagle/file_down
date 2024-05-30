
# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(X, Y, Z):
    return (X - 2*Z)//(Y + Z)

x, y, z = map(int, input().split())
print(solve(x, y, z))

