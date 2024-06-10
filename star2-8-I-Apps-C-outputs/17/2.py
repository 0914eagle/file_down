
n, k = map(int, input().split())
if n % 2 == 1:
    print("1" * (n - k) + "0" * k)
else:
    print("1" * n)

