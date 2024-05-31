
def find_number(m, n, p, q):
    for i in range(10**(m-n-1), 10**(m-n)):
        num = int(str(i) + str(p))
        if num * q == int(str(i) + str(num)[:-n]):
            return num
    return "IMPOSSIBLE"

# Input
m, n, p, q = map(int, input().split())

# Output
print(find_number(m, n, p, q))
