
def max_elements_array_b(p):
    p = str(p)
    n = len(p)
    ans = 1
    for i in range(1, n):
        a = int(p[:i])
        b = int(p[i:])
        if b >= a and (b < 10 or int(p[i+1:]) >= a):
            ans = max(ans, n - i)
    return ans

# Input
p = int(input())
# Output
print(max_elements_array_b(p))
