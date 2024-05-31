
def find_number(m, n, p, q):
    for i in range(10**(m-n-1), 10**(m-n)):
        num = int(str(i) + str(p))
        if num * q == int(str(i) + str(p) + str(i)*n):
            return num
    return "IMPOSSIBLE"

# Reading input
m, n, p, q = map(int, input().split())

# Calling the function and printing the result
print(find_number(m, n, p, q))
