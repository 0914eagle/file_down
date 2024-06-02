
def solve_longest_polyline(n, m):
    if n == 0:
        print("0 1\n0 {}\n0 0\n0 {}".format(m, m-1))
    elif m == 0:
        print("1 0\n{} 0\n0 0\n{} 0".format(n, n-1))
    else:
        print("0 0\n{} {}\n{} 0\n0 {}".format(n, m, n, m))

# Input
n, m = map(int, input().split())

# Output
solve_longest_polyline(n, m)
