
b1, q, l, m = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(1, l+1):
    if b1 * q**i > l or b1 * q**i < -l or (b1 * q**i in a):
        continue
    ans += 1
if ans == 0:
    print("inf")
else:
    print(ans)
