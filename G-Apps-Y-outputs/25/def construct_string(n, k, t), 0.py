
def construct_string(n, k, t):
    s = t * (k // (n - 1))
    extra = k % (n - 1)
    if extra == 0:
        return s
    else:
        return s + t[:extra]

# Input
n, k = map(int, input().split())
t = input().strip()

# Output
print(construct_string(n, k, t))
