
q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if (i + k) % 3 == 0 and s[i] != "R":
            ans += 1
        elif (i + k) % 3 == 1 and s[i] != "G":
            ans += 1
        elif (i + k) % 3 == 2 and s[i] != "B":
            ans += 1
    print(ans)

