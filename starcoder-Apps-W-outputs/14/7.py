
# -*- coding: utf-8 -*-


n,m = map(int,input().split())
student = []
for i in range(n):
    student.append(input())
scores = list(map(int,input().split()))
ans = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(student[j][i])
    ans.append(tmp)
ans1 = []
for i in range(m):
    d = {}
    for j in range(len(ans[i])):
        if ans[i][j] not in d:
            d[ans[i][j]] = 1
        else:
            d[ans[i][j]] += 1
    ans1.append(d)
score = []
for i in range(m):
    s = max(ans1[i].values())
    score.append(s)
score1 = 0
for i in range(m):
    score1 += score[i]*scores[i]
print(score1)
