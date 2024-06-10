
for i in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    r, g, b = s.count('R'), s.count('G'), s.count('B')
    ans = min(r, g, b)
    print(ans)

