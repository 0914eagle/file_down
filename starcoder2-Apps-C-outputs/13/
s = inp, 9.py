
s = input()
n = len(s)
ans = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if s[i] == s[j] == s[k]:
                ans += 1
print(ans)
