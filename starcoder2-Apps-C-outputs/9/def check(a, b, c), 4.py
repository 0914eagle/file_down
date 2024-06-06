
def check(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    if len(a) != len(b) or len(a) != len(c) or len(b) != len(c):
        return False
    for i in range(len(a)):
        if a[i] in b or a[i] in c or b[i] in c:
            return False
    return True

p = int(input())

cnt = 0
ans = []
for i in range(1, p):
    for j in range(i + 1, p):
        if check(i, j, i + j):
            cnt += 1
            ans.append((i, j))

print(cnt)
for i in range(min(5000, len(ans))):
    print(ans[i][0], ans[i][1])
