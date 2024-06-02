
def max_original_elements(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        if int(p[i:]) >= int(p[:i]):
            ans += 1
    return ans

p = input().strip()
print(max_original_elements(p))
