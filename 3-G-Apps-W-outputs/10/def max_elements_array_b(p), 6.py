
def max_elements_array_b(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        if int(p[i:]) >= int(p[i-1:]):
            ans += 1
        else:
            break
    return ans

# Input
p = input().strip()

# Output
print(max_elements_array_b(p))
