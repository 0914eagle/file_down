
def solve(p):
    count = 0
    for i in range(1, len(p) - 1):
        if p[i - 1] < p[i] and p[i] < p[i + 1]:
            count += 1
    return count

