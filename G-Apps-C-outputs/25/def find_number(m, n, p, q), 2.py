
def find_number(m, n, p, q):
    for i in range(10**(m-n)-1, 10**(m-n-1)-1, -1):
        candidate = int(str(i) + str(p))
        if candidate * q == int(str(candidate)[n:]):
            return candidate
    return "IMPOSSIBLE"

# Input parsing
m, n, p, q = map(int, input().split())

result = find_number(m, n, p, q)
print(result)
