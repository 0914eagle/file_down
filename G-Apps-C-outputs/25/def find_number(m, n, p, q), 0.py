
def find_number(m, n, p, q):
    for i in range(10**(m-n), 10**(m-n+1)):
        number = int(str(i) + str(p))
        if number * q == int(str(number)[n:]):
            return number
    return "IMPOSSIBLE"

# Input
m, n, p, q = map(int, input().split())

# Output
print(find_number(m, n, p, q))
