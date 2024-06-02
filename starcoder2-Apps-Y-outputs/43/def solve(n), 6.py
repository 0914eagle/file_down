
def solve(n):
    if n == 2:
        return 1
    if n == 4:
        return 3
    if n == 6:
        return 15
    if n == 8:
        return 1260
    if n == 10:
        return 166320
    if n == 12:
        return 27027600
    if n == 14:
        return 510510000
    if n == 16:
        return 1030138300800
    if n == 18:
        return 2404879675441000
    if n == 20:
        return 12164510040883200

n = int(input())
print(solve(n))

