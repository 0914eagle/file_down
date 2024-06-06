
s = input()
n = len(s)

ans = 0
for i in range(n):
    for j in range(i, n):
        if s[i] == s[j]:
            ans += 1

print(ans)
