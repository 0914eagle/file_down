
def max_elements_array_p(p):
    p = str(p)
    n = len(p)
    ans = 1
    for i in range(1, n):
        if int(p[i:]) % 10 ** (n - i - 1) == int(p[:i]):
            ans += 1
    return ans

# Read input
p = int(input().strip())

# Call the function and print the result
print(max_elements_array_p(p))
