
def solve(n, a):
    # Your code goes here.
    # Return the answer as a tuple (y, z).

n = int(input())
a = list(map(int, input().split()))
y, z = solve(n, a)
print(y, z)

