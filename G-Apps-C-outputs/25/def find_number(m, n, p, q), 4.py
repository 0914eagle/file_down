
def find_number(m, n, p, q):
    for i in range(1, 10**m):
        num_str = str(i)
        if len(num_str) < m:
            continue
        if int(num_str[:n] + str(p) + num_str[n:]) * q == i:
            return i
    return "IMPOSSIBLE"

# Input
m, n, p, q = map(int, input().split())

# Output
print(find_number(m, n, p, q))
