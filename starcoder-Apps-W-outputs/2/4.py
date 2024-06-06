
n, h, m, k = map(int, input().split())
li = []
for i in range(n):
    h_i, m_i = map(int, input().split())
    li.append((h_i*m + m_i, i+1))
li.sort()
li = [i[1] for i in li]
t = m//2 - k
flag = True
ans = 0
for i in range(0, n, 2):
    if li[i]%(m//2) > t:
        flag = False
        break
if flag:
    print(0, 0)
    print()
else:
    ans += 1
    print(1, 0)
    print(li[0])
