
def find_number(m, n, p, q):
    for i in range(10**(m-n)-1, 10**(m-n-1)-1, -1):
        num = int(str(i) + str(p))
        if num * q == int(str(num)[n:]):
            return num
    return "IMPOSSIBLE"

# Taking input
m, n, p, q = map(int, input().split())

# Calling the function and printing the result
print(find_number(m, n, p, q))
