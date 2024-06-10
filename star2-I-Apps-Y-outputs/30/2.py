
s = input()
n = len(s)
ans = 0
for i in range(1 << (n - 1)):
    num = int(s[0])
    for j in range(n - 1):
        if (i >> j) & 1:
            num += int(s[j + 1])
        else:
            num *= 10
            num += int(s[j + 1])
    ans += num
print(ans)

