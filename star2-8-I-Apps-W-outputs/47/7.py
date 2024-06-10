
n, a, b, c, d = map(int, input().split())
def count_squares(n, a, b, c, d):
    res = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            for z in range(1, n+1):
                for t in range(1, n+1):
                    if (x + y + b + d == a + b + c + d and
                        x + z + a + c == a + b + c + d and
                        y + t + b + d == a + b + c + d and
                        z + t + a + c == a + b + c + d):
                        res += 1
    return res
print(count_squares(n, a, b, c, d))

