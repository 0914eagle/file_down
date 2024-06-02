
def paint(n, k):
    if n == 1:
        return k
    else:
        return (k-1) * (paint(n-1, k) + paint(n-2, k))

n, k = map(int, input().split())
print(paint(n, k))

