
#coding: utf-8

n = int(input())

st = []
for i in range(n):
    st.append(input())

st.sort(key=lambda x: len(x))

ans = 1
for i in range(1, n):
    flag = True
    for j in range(len(st[i-1])):
        if st[i-1][j] != st[i][j]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
