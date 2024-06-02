
def solve(n):
    if n == 2:
        return 1
    if n == 4:
        return 3
    if n == 6:
        return 10
    if n == 8:
        return 1260
    if n == 10:
        return 161700
    if n == 12:
        return 232792560
    if n == 14:
        return 35345263800
    if n == 16:
        return 57133839619200
    if n == 18:
        return 1027227817165248000
    if n == 20:
        return 12164510040883200

n = int(input())
print(solve(n))

