
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for j in range(n-1):
        if s[j] == 'A':
            ans += 1
            s = s[:j+1] + 'A' + s[j+1:]
    print(ans)
