
def construct_string(n, k, t):
    prefix = t
    for i in range(1, n):
        if t[i:] == t[:n - i]:
            prefix = t[:i]
            break
    s = prefix + (t * (k - 1))
    return s

# Read input
n, k = map(int, input().split())
t = input().strip()

# Call the function and print the output
print(construct_string(n, k, t))
