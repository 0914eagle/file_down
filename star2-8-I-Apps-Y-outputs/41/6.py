
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
if (max(q) - min(q) + 1) // 2 >= k:
    print("NO")
else:
    print("YES")
    s = [0] * n
    chars = [0] * 26
    for i in range(n):
        chars[ord(s[q[i] - 1]) - ord('a')] = 1
    c = 0
    for i in range(n):
        while chars[c] == 1:
            c += 1
        s[p[i] - 1] = chr(ord('a') + c)
        chars[c] = 1
    print("".join(s))

