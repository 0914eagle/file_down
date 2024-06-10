
n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
for i in range(n):
    if s1[i] == 0 and s2[i] == 0:
        s1[i] = 1
        s2[i] = 1

for i in range(n):
    if s1[i] == 0:
        s1[i] = s2[i]
    elif s2[i] == 0:
        s2[i] = s1[i]

if s1 > s2:
    print((10 ** 9 + 7 - 1) // 2)
else:
    print(0)

