
# input
# 2 10
# half
# halfplus

n, p = map(int, input().split())
#n = 2
#p = 10

half = 0
halfplus = 0
for i in range(n):
    s = input()
    #half = 0
    #halfplus = 0
    #half
    #halfplus
    if s == "half":
        half += 1
    else:
        half += 1
        halfplus += 1
    print(half, halfplus)
print(half, halfplus)

half = half // 2
halfplus = halfplus // 2
print(half, halfplus)

ans = half * p + halfplus * (p + p // 2)
print(ans)
