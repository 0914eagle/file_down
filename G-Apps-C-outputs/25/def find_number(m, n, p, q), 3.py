
def find_number(m, n, p, q):
    for i in range(10**(m-1), 10**m):
        num_str = str(i)
        if len(num_str) >= n + len(str(p)):
            truncated_num = int(num_str[n:] + str(p))
            if truncated_num * q == i:
                return i
    return "IMPOSSIBLE"

# Input
m, n, p, q = map(int, input().split())

# Output
print(find_number(m, n, p, q))
