
def max_chessmen(n, m):
    if n < 2 or m < 2:
        return 0
    if n == 2 and m == 2:
        return 0
    max_chessmen = (n // 2) * (m // 2) * 2
    if n % 2 == 1 and m % 2 == 1:
        return max_chessmen + 2
    return max_chessmen

n, m = map(int, input().split())
print(max_chessmen(n, m))
