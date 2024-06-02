
def max_elements_array_b(p):
    n = len(p)
    ans = 1
    for i in range(1, n):
        num1 = int(p[:i])
        num2 = int(p[i:])
        if num1 >= num2:
            ans = max(ans, 2)
        else:
            break
    print(ans)

# Input
p = input().strip()

# Call the function
max_elements_array_b(p)
