
n, d_m = map(int, input().split())
d = list(map(int, input().split()))

k = 0
for i in range(n):
    if d[i] <= d_m:
        k = n - i
        break

if k == 0:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in {} years!".format(k))
