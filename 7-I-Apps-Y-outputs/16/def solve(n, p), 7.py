
def solve(n, p):
    # Write your code here
    count = 0
    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            count += 1
    return count

