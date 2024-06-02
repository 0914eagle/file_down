
def max_original_elements(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        num1 = int(p[:i])
        num2 = int(p[i:])
        if num1 <= num2:
            ans = max(ans, n - i)
    return ans

p = input().strip()
print(max_original_elements(p))
