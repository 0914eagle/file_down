
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for j in range(n-1):
        if s[j] == 'A' and s[j+1] == 'P':
            ans += 1
            s = s[:j+1] + 'A' + s[j+2:]
    print(ans)
