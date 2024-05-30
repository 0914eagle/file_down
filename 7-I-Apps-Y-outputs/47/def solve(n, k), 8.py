
def solve(n, k):
    for i in range(1, k+1):
        if n%i == 0:
            return n//i

