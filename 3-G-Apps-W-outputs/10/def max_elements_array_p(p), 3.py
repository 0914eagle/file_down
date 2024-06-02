
def max_elements_array_p(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        if int(p[i:]) % 10**(n-i) == int(p[:i]):
            ans += 1
    return ans

# Input
p = input().strip()

# Output
print(max_elements_array_p(p))
