
def check(n):
    n = str(n)
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j and n[i] == n[j]:
                return False
    return True

n = int(input())
ans = []
for i in range(1, n):
    if check(i) and check(n - i) and i < n - i:
        ans.append((i, n - i))
print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
