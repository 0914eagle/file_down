
def construct_string(n, k, t):
    s = t
    while k > 1:
        i = 1
        while i < n and t[:i] != t[-i:]:
            i += 1
        s += t[i:]
        k -= 1
    return s

# Read input
n, k = map(int, input().split())
t = input().strip()

# Construct the string
result = construct_string(n, k, t)
print(result)
