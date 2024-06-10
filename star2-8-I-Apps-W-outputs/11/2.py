
def grisha_xor(n, k):
    xor = 0
    for bit in range(50, -1, -1):
        ones = 0
        for i in range(1, n + 1):
            if (i >> bit) & 1:
                ones += 1
        if ones > k:
            continue
        xor |= (1 << bit)
        k -= ones
    return xor

n, k = map(int, input().split())
print(grisha_xor(n, k))

