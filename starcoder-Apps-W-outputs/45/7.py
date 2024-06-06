
s1 = input()
s2 = input()
n = len(s1)
if s1 == s2:
    print(1)
elif '?' in s2:
    ans = 1
    for i in range(n):
        if s2[i] != s1[i] and s2[i] != '?':
            ans /= 2
    print(ans)
else:
    print(0)
