
def max_elements_array(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        x = int(p[:i])
        y = int(p[i:])
        if y >= x and y - x <= 1:
            ans = max(ans, n - i)
    return ans

# Input
p = input().strip()

# Output
print(max_elements_array(p))
