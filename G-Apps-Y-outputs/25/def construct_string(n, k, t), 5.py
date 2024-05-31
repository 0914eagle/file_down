
def construct_string(n, k, t):
    s = t
    for i in range(1, n):
        prefix = t[i:]
        if t.endswith(prefix):
            s = t[:i]
            break
    return s * k

# Read input
n, k = map(int, input().split())
t = input().strip()

# Output result
result = construct_string(n, k, t)
print(result)
