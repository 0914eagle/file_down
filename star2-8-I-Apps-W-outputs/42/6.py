
m, d = map(int, input().split())
a = int(input())
b = int(input())
num = 0
for i in range(a, b+1):
    if i%m != 0:
        continue
    cnt = 0
    s = str(i)
    for j in range(len(s)):
        if int(s[j]) == d and j%2 == 0:
            cnt += 1
    if cnt == 0:
        continue
    num = (num + cnt) % (10**9 + 7)
print(num)

