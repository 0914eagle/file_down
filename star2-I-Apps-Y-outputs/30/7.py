
s = input()
ans = 0
for i in range(1 << len(s) - 1):
    tmp = s[0]
    for j in range(1, len(s)):
        if i & (1 << (j - 1)):
            tmp += "+"
        tmp += s[j]
    ans += eval(tmp)
print(ans)

