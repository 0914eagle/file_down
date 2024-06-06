
a, b = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
f_reverse = [0 for i in range(a + 1)]
for i in range(a):
    f_reverse[f[i]] = i + 1
ans = [0 for i in range(b)]
for i in range(b):
    if f_reverse[b[i]] == 0:
        print("Impossible")
        exit()
    ans[i] = f_reverse[b[i]]
for i in ans:
    print(i, end = ' ')
