
def construct_string(n, k, t):
    s = ""
    for i in range(1, n+1):
        if t[:i] == t[-i:]:
            common_suffix = t[-i:]
            break
    
    s += t
    for _ in range(k-1):
        s += common_suffix
    
    return s

# Read input
n, k = map(int, input().split())
t = input().strip()

# Construct and print the string
print(construct_string(n, k, t))
