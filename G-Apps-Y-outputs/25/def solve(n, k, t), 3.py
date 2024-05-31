
def solve(n, k, t):
    full_str = t * k
    for i in range(n, 0, -1):
        if t[:i] == t[-i:]:
            return t + full_str[i:]
    return t + full_str

# Input parsing
n, k = map(int, input().split())
t = input().strip()

# Call the function and print the result
result = solve(n, k, t)
print(result)
