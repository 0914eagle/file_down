
def f(n):
    if n == 2:
        return 1
    else:
        return (n-1) * f(n-2)

n = int(input())
print(f(n))
