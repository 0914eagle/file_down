
def min_rows_for_mirroring(n, m, a):
    def is_mirrored(a):
        x = len(a)
        y = len(a[0])
        for i in range(x):
            for j in range(y):
                if a[i][j] != a[2*x-1-i][j]:
                    return False
        return True

    for x in range(1, n+1):
        if n % x == 0:
            b = [a[i][:] for i in range(x)]
            if is_mirrored(b):
                return x

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(min_rows_for_mirroring(n, m, a))
