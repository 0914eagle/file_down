
n, k = list(map(int, input().split()))
if k % 2 == 0:
    s = "0" * k + "1" * (n - k)
else:
    s = "1" * k + "0" * (n - k)
print(s)

